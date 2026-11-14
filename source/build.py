import math, re, sys
from collections import OrderedDict, Counter
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from model import *
from descs import DESC

OUT = sys.argv[1]

# ------------------------------------------------------------ parse inventory
ROWS, INV = [], {}
for bi, (title, ctx, domain, defcat, text) in enumerate(BATCHES, 1):
    for line in text.strip().splitlines():
        t, label, parent, profile, flags, cat = [x.strip() for x in line.split("|")]
        assert profile in P, profile
        assert t not in INV, t
        r = dict(table=t, label=label, parent=parent, profile=profile, flags=flags,
                 cat=cat or defcat, ctx=ctx, domain=domain, batch=bi, batch_title=title)
        ROWS.append(r); INV[t] = r
assert len(ROWS) == 322, len(ROWS)
assert set(DESC) == set(INV), (set(INV)-set(DESC), set(DESC)-set(INV))

def lbl(t):
    if t in INV: return INV[t]["label"]
    return EXTRA_LABELS[t]

MAND = {"M": "Mandatory", "O": "Optional"}
def mand(m): return MAND.get(m, m)

REL = OrderedDict()   # (parent, type, child) -> dict
def reg_rel(parent, rtype, child, direction, m, by):
    k = (parent, rtype, child)
    e = REL.setdefault(k, dict(dir=set(), mand=[], by=[], n=0))
    e["dir"].add(direction); e["n"] += 1
    if mand(m) not in e["mand"]: e["mand"].append(mand(m))
    for b in by.split(" / "):
        if b not in e["by"]: e["by"].append(b)

def render(rel, self_t):
    parent, rtype, child, kind, m, by = rel
    p = self_t if parent == S else parent
    c = self_t if child == S else child
    if kind == "lat": d = "Lateral"
    elif (kind == "down" and parent == S) or (kind == "up" and child == S): d = "Downstream"
    else: d = "Upstream"
    reg_rel(p, rtype, c, d, m, by)
    return f"{lbl(p)} [{p}] -> {rtype} -> {lbl(c)} [{c}] ({mand(m)})"

ATTR_USE = Counter()
IDENT = re.compile(r"^[a-z_]+$")
def attr_cell(items):
    for it in items:
        if IDENT.match(it):
            assert it in ATTR, f"attribute not in dictionary: {it}"
            ATTR_USE[it] += 1
    return "\n".join(items)

# ------------------------------------------------------------ build Sheet 1 records
RECS = []
for r in ROWS:
    t, L = r["table"], r["label"]
    p = P[r["profile"]]; ov = OV.get(t, {}); m = {**p, **ov}
    fl = r["flags"]
    par = r["parent"]
    inherits = par in INV and INV[par]["profile"] == r["profile"]
    inh = f"Inherits from {lbl(par)} [{par}]" if inherits else None
    V = f"{lbl(m['via'])} [{m['via']}]" if "via" in m else ""
    if r["profile"] in ("component", "db_catalog"): assert "via" in m, t
    fmt = lambda s: s.replace("{L}", L).replace("{V}", V)

    def col(c):
        add = ov.get(c + "_add", [])
        if c in ov: return attr_cell(ov[c] + add)
        if inherits: return attr_cell([inh] + add)
        return attr_cell(p[c] + add)
    req, rec, key = col("req"), col("rec"), col("key")
    own = inh if inherits else attr_cell(m["own"])
    life = inh if inherits else attr_cell(m["life"])
    if inherits and "ident" not in ov:
        ident = f"Inherits the identification rule of {lbl(par)} [{par}] unless a class-specific rule is active in CI Class Manager."
    else:
        ident = m["ident"]

    ups, downs, lats = [], [], []
    for rel in m["rels"]:
        s = render(rel, t)
        {"up": ups, "down": downs, "lat": lats}[rel[3]].append(s)
    if m.get("up_text"): ups.append(fmt(m["up_text"]))
    if m.get("down_text"): downs.append(fmt(m["down_text"]))
    if "via" in m: ups.append(f"Context is inherited through {V}.")
    assert ups and downs, (t, ups, downs)

    notes = []
    if m.get("note"): notes.append(m["note"])
    if "a" in fl: notes.append("Abstract or holding class: do not keep records directly in this class; reclassify to the most specific child class.")
    if "v" in fl: notes.append("Flagged (verify) in the inventory: confirm table name, label and availability in the instance. Logged on Sheet 5.")
    if "q" in fl: notes.append("Parent class not confirmed: check Extends in CI Class Manager.")
    for s in lats: notes.append("Lateral: " + s)
    if not notes: notes.append("None")

    conf = m["conf"]
    if "L" in fl or "v" in fl: conf = "Low"
    elif "q" in fl and conf == "High": conf = "Medium"

    if t in CLASS_MODELS: shipped = "CMDB CI Class Models app"
    elif "v" in fl: shipped = "Verify in instance (plugin or CMDB CI Class Models app)"
    else: shipped = "Base platform"

    RECS.append(dict(r=r, conf=conf, cells=[
        ov.get("ctx", r["ctx"]), ov.get("domain", r["domain"]), r["cat"], L, t,
        par + (" (verify)" if ("q" in fl or "v" in fl) else ""), shipped, m["dep"], "Y" if "P" in fl else "N", m["source"],
        req, rec, own, life, key,
        fmt(ident), "\n".join(ups), "\n".join(downs), fmt(m["host"]), fmt(m["trace"]), fmt(m["orphan"]), m["stale"], m["dup"],
        m["audit"], m["csdm"], m["cert"],
        m["gate"], "\n".join(notes), conf]))

# core chain relationships always present on Sheet 2
for pa, ty, ch in [("cmdb_ci_business_app", CONS, "cmdb_ci_service_auto"), ("service_offering", DEP, "cmdb_ci_service_auto"),
                   ("cmdb_ci_service_auto", DEP, "cmdb_ci_appl"), ("cmdb_ci_appl", RUN, "cmdb_ci_server"),
                   ("cmdb_ci_server", VIRT, "cmdb_ci_vm_instance"), ("cmdb_ci_vm_instance", REG, "cmdb_ci_esx_server"),
                   ("cmdb_ci_vm_instance", HOST, "cmdb_ci_logical_datacenter"), ("cmdb_ci_logical_datacenter", HOST, "cmdb_ci_cloud_service_account"),
                   ("cmdb_ci_server", LOC, "cmdb_ci_rack"), ("cmdb_ci_rack", LOC, "cmdb_ci_computer_room"), ("cmdb_ci_computer_room", LOC, "cmdb_ci_datacenter")]:
    assert (pa, ty, ch) in REL, (pa, ty, ch)

# ------------------------------------------------------------ styles
ARIAL = "Arial"
F_BODY = Font(name=ARIAL, size=9)
F_HEAD = Font(name=ARIAL, size=9, bold=True, color="FFFFFF")
F_BAND = Font(name=ARIAL, size=11, bold=True, color="FFFFFF")
F_BOLD = Font(name=ARIAL, size=9, bold=True)
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
HEADA = Alignment(wrap_text=True, vertical="center", horizontal="center")
def fill(h): return PatternFill("solid", start_color=h, end_color=h)

GROUPS = [("Identity", 10, "1F4E79", "DDEBF7"), ("Completeness", 5, "375623", "E2EFDA"),
          ("Correctness", 8, "9C5700", "FFF2CC"), ("Compliance", 3, "5B2C83", "E9DDF3"), ("Governance", 3, "404040", "EDEDED")]
HEADERS = ["Context", "CSDM 5.0 domain", "Category", "Class label", "Table name", "Parent class (extends)", "Shipped by",
           "Independent or dependent class", "Principal class (Y/N)", "Typical population source",
           "Required attributes", "Recommended attributes", "Ownership attributes", "Lifecycle attributes", "Class-specific key attributes",
           "Identification rule", "Mandatory upstream relationship", "Mandatory downstream relationship", "Hosting / containment rule",
           "Three-context trace path", "Orphan rule", "Staleness rule", "Duplicate risk and reconciliation note",
           "Audit / desired-state checks", "CSDM 5.0 compliance check", "Certification owner and frequency",
           "Onboarding gate", "Notes and assumptions", "Confidence"]
WIDTHS = [14, 17, 20, 26, 30, 26, 22, 14, 10, 28,
          26, 30, 22, 22, 28,
          46, 52, 52, 36, 60, 40, 38, 42,
          42, 44, 24,
          44, 46, 11]
assert len(HEADERS) == len(WIDTHS) == 29

def row_height(values, widths, minh=15):
    lines = 1
    for v, w in zip(values, widths):
        if v is None: continue
        n = sum(max(1, math.ceil(len(part) / max(1.0, w * 1.15))) for part in str(v).split("\n"))
        lines = max(lines, n)
    return min(409, max(minh, 12.2 * lines + 4))

wb = Workbook()

# ------------------------------------------------------------ Sheet 1
ws = wb.active; ws.title = "Class Data Model"
c0 = 1
for name, n, dark, light in GROUPS:
    ws.merge_cells(start_row=1, start_column=c0, end_row=1, end_column=c0 + n - 1)
    cell = ws.cell(1, c0, name); cell.font = F_BAND; cell.fill = fill(dark); cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    for c in range(c0, c0 + n):
        h = ws.cell(2, c, HEADERS[c - 1]); h.font = F_HEAD; h.fill = fill(dark); h.alignment = HEADA; h.border = BORDER
    c0 += n
ws.row_dimensions[1].height = 20; ws.row_dimensions[2].height = 42
colfill = []
for name, n, dark, light in GROUPS: colfill += [fill(light)] * n
CONF_FILL = {"High": fill("C6EFCE"), "Medium": fill("FFEB9C"), "Low": fill("F8CBAD")}
for i, rec in enumerate(RECS):
    rr = i + 3
    for c, v in enumerate(rec["cells"], 1):
        cell = ws.cell(rr, c, v); cell.font = F_BODY; cell.alignment = WRAP; cell.border = BORDER; cell.fill = colfill[c - 1]
    ws.cell(rr, 4).font = F_BOLD
    ws.cell(rr, 29).fill = CONF_FILL[rec["conf"]]
    ws.row_dimensions[rr].height = row_height(rec["cells"], WIDTHS)
for c, w in enumerate(WIDTHS, 1): ws.column_dimensions[get_column_letter(c)].width = w
ws.freeze_panes = "F3"
ws.auto_filter.ref = f"A2:{get_column_letter(29)}{len(RECS) + 2}"
ws.sheet_view.zoomScale = 90

def simple_sheet(title, headers, widths, rows, dark="1F4E79", freeze="A2"):
    s = wb.create_sheet(title)
    for c, h in enumerate(headers, 1):
        x = s.cell(1, c, h); x.font = F_HEAD; x.fill = fill(dark); x.alignment = HEADA; x.border = BORDER
    s.row_dimensions[1].height = 30
    for i, row in enumerate(rows, 2):
        for c, v in enumerate(row, 1):
            x = s.cell(i, c, v); x.font = F_BODY; x.alignment = WRAP; x.border = BORDER
        s.row_dimensions[i].height = row_height(row, widths)
    for c, w in enumerate(widths, 1): s.column_dimensions[get_column_letter(c)].width = w
    s.freeze_panes = freeze
    s.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(rows) + 1}"
    return s

# ------------------------------------------------------------ Sheet 2
def mech(t):
    if t.startswith("Reference field"): return "Reference field"
    if t.startswith("Service CI association"): return "Association table"
    if t.startswith("Software instance"): return "Install record table"
    if t.startswith("Verify"): return "To be verified"
    return "CI relationship (cmdb_rel_ci)"
rel_rows = []
for (pa, ty, ch), e in REL.items():
    d = e["dir"] - {"Lateral"} or e["dir"]
    if len(d) > 1:
        print("direction conflict resolved to Downstream:", pa, ty, ch)
        d = {"Downstream"}
    mm = "Mandatory" if "Mandatory" in e["mand"] else "; ".join(e["mand"])
    rel_rows.append([lbl(pa), pa, ty, lbl(ch), ch, list(d)[0], mm, " / ".join(e["by"]), mech(ty)])
rel_rows.sort(key=lambda x: (x[0].lower(), x[2], x[3].lower()))
s2 = simple_sheet("Relationship Matrix",
    ["Parent class", "Parent table", "Relationship type (Parent::Child)", "Child class", "Child table",
     "Direction, reading parent to child", "Mandatory or optional", "Created by", "Mechanism"],
    [30, 34, 40, 30, 34, 18, 30, 44, 24], rel_rows, freeze="C2")
DIRF = {"Downstream": fill("DDEBF7"), "Upstream": fill("FFF2CC"), "Lateral": fill("EDEDED")}
for i, row in enumerate(rel_rows, 2): s2.cell(i, 6).fill = DIRF[row[5]]

# ------------------------------------------------------------ Sheet 3
PATTERNS = [
 ["On-premises server stack", "Application installed on physical or virtual servers in own data centers",
  "Business Application", "Service Instance (Mapped or Calculated Application Service) + Business Service Offering",
  "Application / Database Instance -> Server -> VM Instance -> ESX Server -> Rack -> Data Center",
  "Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> Application / Database Instance -> Runs on::Runs -> Server -> Virtualized by::Virtualizes -> VM Instance -> Registered on::Has registered -> ESX Server -> Located in::Houses -> Rack -> Located in::Houses -> Computer Room -> Located in::Houses -> Data Center",
  "Discovery (IP-based), Service Mapping, vCenter discovery, DCIM import",
  "Physical servers skip the VM Instance and ESX steps and go straight to Rack. Ownership of servers comes from a Dynamic CI Group under a Technology Management Offering."],
 ["Cloud IaaS", "Virtual machines in AWS, Azure or GCP running an installed application",
  "Business Application", "Service Instance (Tag-Based or Mapped) + Business Service Offering",
  "Application -> Server -> VM Instance -> Logical Datacenter -> Cloud Service Account",
  "Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> Application -> Runs on::Runs -> Server -> Virtualized by::Virtualizes -> VM Instance -> Hosted on::Hosts -> Logical Datacenter (AWS / Azure / Google Datacenter) -> Hosted on::Hosts -> Cloud Service Account",
  "Cloud discovery or Service Graph Connector, plus Discovery / Agent Client Collector for the guest OS",
  "Without guest discovery there is no Server or Application CI: the Service Instance then links to the VM Instance through tags (svc_ci_assoc)."],
 ["Cloud PaaS", "Managed services with no server to manage: cloud databases, object storage, functions, messaging",
  "Business Application", "Service Instance (Tag-Based) or Data Service Instance + Business Service Offering",
  "Cloud resource (Cloud Database, Cloud Object Storage, Cloud Function...) -> Logical Datacenter -> Cloud Service Account",
  "Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by (or svc_ci_assoc from tags) -> cloud resource -> Hosted on::Hosts -> Logical Datacenter -> Hosted on::Hosts -> Cloud Service Account",
  "Cloud discovery or Service Graph Connector; tag-based service mapping",
  "Tags are the only practical source of business context. Untagged resources fail the onboarding gate."],
 ["Kubernetes", "Containerised workloads on managed or self-hosted clusters",
  "Business Application", "Service Instance (Tag-Based, by label) + Business Service Offering",
  "Workload (Service / Deployment / StatefulSet) -> Namespace -> Cluster -> Logical Datacenter -> Cloud Service Account; Pod -> Node",
  "Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> Kubernetes workload -> (contained by) Kubernetes Namespace -> (contained by) Kubernetes Cluster -> Hosted on::Hosts -> Logical Datacenter -> Hosted on::Hosts -> Cloud Service Account",
  "Kubernetes discovery (agent or pattern), cloud discovery, label-based service mapping",
  "Govern at workload and namespace level. Pods and containers are short-lived: keep them out of the gate and give them a short staleness window. All Kubernetes class names need confirming in the instance."],
 ["SaaS", "Application delivered by a vendor; no infrastructure visible to us",
  "Business Application (install type: cloud / SaaS)", "Service Instance (manual, one per tenant or environment) + Business Service Offering",
  "None owned. Optional: integration endpoints, identity provider application, certificates",
  "Business Application -> Consumes::Consumed by -> Service Instance -> (optional) Depends on::Used by -> integration / identity components that we do run",
  "Manual; SaaS management or SAM connector for subscription data",
  "The trace stops at the Service Instance. Record the vendor on the Service Instance and treat the infrastructure context as 'vendor managed'; the downstream rule is waived by exception, recorded on the Service Instance."],
 ["Network service", "Shared connectivity: LAN, WAN, firewall, load balancing, circuits",
  "Business Application (consumes connectivity indirectly) or Business Service Offering for network",
  "Network Service Instance / Connection Service Instance + Technology Management Offering -> Dynamic CI Group",
  "Network Gear (router, switch, firewall, load balancer) -> Rack / location; Circuit -> provider",
  "Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> Network Service Instance -> Depends on::Used by -> Network Gear -> Located in::Houses -> Rack -> Data Center; Technology Management Service -> Technology Management Offering -> Contains::Contained by -> Dynamic CI Group -> svc_ci_assoc -> Network Gear",
  "Discovery (SNMP), network controller integration, manual for circuits",
  "Network devices serve many applications, so ownership through the Dynamic CI Group is mandatory; the link to individual Service Instances is added where Service Mapping finds it."],
 ["End-user device", "Laptops, desktops, mobiles, printers, phones",
  "User, department and cost centre from assigned_to; Business Service Offering for workplace services",
  "Technology Management Offering (end-user computing) -> Dynamic CI Group",
  "Personal Computer / Handheld / Printer -> location and asset",
  "Business Service (Workplace) -> Business Service Offering -> Technology Management Service -> Technology Management Offering -> Contains::Contained by -> Dynamic CI Group -> svc_ci_assoc -> Personal Computer -> assigned_to (user) / location / asset",
  "Endpoint management connector (Intune, SCCM, Jamf), Agent Client Collector, asset receiving",
  "No Business Application or per-device Service Instance. Business context comes from the assigned user; the application context is the offering that supports the device."],
]
simple_sheet("Three-Context Patterns",
    ["Pattern", "When it applies", "Business context", "Application context", "Infrastructure context", "Full chain", "Populated by", "Governance note"],
    [22, 34, 30, 40, 44, 80, 36, 60], PATTERNS, freeze="B2")

# ------------------------------------------------------------ Sheet 4
attr_rows = [[a, ATTR[a][0], ATTR[a][1], ATTR[a][2], ATTR[a][3], ATTR_USE[a]] for a in ATTR if ATTR_USE[a]]
attr_rows.sort(key=lambda x: x[0])
simple_sheet("Attribute Dictionary",
    ["Column name", "Label", "Table where it is defined", "Type", "Why it matters", "Class rows that list it"],
    [30, 28, 44, 30, 70, 14], attr_rows, freeze="B2")

# ------------------------------------------------------------ Sheet 5
ASSUMPTIONS = [
 "Scope is the 322 classes in the prompt inventory, one row each on 'Class Data Model'. Nothing was checked against a live instance; the Confidence column and 'Verify in instance' markers show where confirmation is needed.",
 "'Required attributes' are the fields this model says must be enforced (dictionary mandatory or data policy). The base platform marks very few CMDB fields mandatory, so most of these need to be configured.",
 "'Recommended attributes' are meant to be set as recommended fields per class in CI Class Manager (Health > Completeness) so the Completeness score measures them.",
 "The three C's follow CMDB Health: Completeness = required and recommended fields; Correctness = duplicate, orphan and stale; Compliance = audit results. Mandatory upstream and downstream relationships are enforced through orphan rules and audits.",
 "Staleness durations are proposed design values (30 days discovered infrastructure, 7 days cloud, 1 to 3 days ephemeral container objects, 60 days end-user and OT, 180 to 365 days manually maintained). The platform default is 60 days.",
 "Child classes show 'Inherits from <parent>' plus what they add, as the prompt asked. Read up the parent chain for the full attribute list.",
 "Relationship types are standard CI relationship types. The business-to-application links (Consumes::Consumed by, Depends on::Used by, Contains::Contained by, offering parent reference) follow CSDM guidance; confirm against the CSDM 5.0 documentation for the release in use.",
 "Physical placement is modelled with Located in::Houses (server to rack to room to data center). Confirm the relationship type against the DCIM integration in use.",
 "Identification rules are described from base-system behaviour. CMDB CI Class Models updates change identifier entries, so each rule must be read from CI Class Manager before it is relied on.",
 "Parent classes marked (verify) are best knowledge of the class hierarchy and were not confirmed.",
 "The new Service Instance types (Data, Network, Connection, Operational Process, Facility) are modelled as full Service Instances. Confirm that the release in use populates service CI associations for them.",
 "Three classes listed in the business batch are placed in other contexts: AI & Model Application (infrastructure application CI), AI Function and Environment (application context).",
 "Certification owners and frequencies are proposals to be agreed with the customer's data governance board.",
 "Technology Management Offerings with Dynamic CI Groups are assumed to exist for every infrastructure tower (compute, network, storage, virtualisation, cloud, containers, end-user, facilities). Where they do not, the upstream rule for shared infrastructure cannot pass.",
]
QUESTIONS = [
 "Which ServiceNow release and which version of CMDB CI Class Models is installed? (Decides which of the flagged classes exist.)",
 "Which population sources are in use (Discovery, Agent Client Collector, Service Graph Connectors for AWS / Azure / GCP, Intune, SCCM, Jamf), and which is authoritative per class?",
 "Is Service Mapping licensed, and will services be built top-down, tag-based, or calculated?",
 "What is the cloud tagging standard (keys for application, environment, owner, cost centre), and is it enforced by policy in the cloud accounts?",
 "What is the naming standard and environment list for Service Instances?",
 "Is APM or an EA tool the source for Business Applications, Business Capabilities and Information Objects?",
 "Are Technology Management Services, Offerings and Dynamic CI Groups already defined per infrastructure tower?",
 "Has the instance moved to the CSDM life cycle fields (life_cycle_stage, life_cycle_stage_status), or are install_status and operational_status still the working fields?",
 "Is there a DCIM source for racks, rooms and data centers, and how does it relate hardware to racks?",
 "Are OT, IoT and medical devices in scope for this CMDB?",
 "Which ephemeral classes (pods, containers, replica sets, snapshots) should be excluded from the onboarding gate or from the CMDB altogether?",
 "Which classes should be Principal Classes for health reporting and task selection?",
 "Who certifies each context, how often, and with which tool (Data Certification, CMDB Data Manager policies, attestation)?",
 "For SaaS applications, is a vendor-managed exception to the downstream rule acceptable to the governance board?",
]
s5 = []
for i, a in enumerate(ASSUMPTIONS, 1): s5.append(["Assumption", f"A{i:02d}", "All", a, "Confirm or correct"])
n = 0
for rec in RECS:
    r = rec["r"]
    if "v" in r["flags"]:
        n += 1
        s5.append(["Class to verify", f"V{n:02d}", f"{r['label']} [{r['table']}]",
                   "Table name was not confirmed from product documentation. It may be named differently, or need a plugin or the CMDB CI Class Models app.",
                   "Look up the class in CI Class Manager; correct the table name, parent and identification rule on Sheet 1"])
n = 0
for rec in RECS:
    r = rec["r"]
    if rec["conf"] == "Low" and "v" not in r["flags"]:
        n += 1
        s5.append(["Low-confidence row", f"L{n:02d}", f"{r['label']} [{r['table']}]",
                   "Attributes, identification or relationships for this class are placeholders marked 'Verify in instance'.",
                   "Review the class in the instance and complete the row"])
for i, q in enumerate(QUESTIONS, 1): s5.append(["Question for the customer", f"Q{i:02d}", "All", q, "Answer needed before the model is baselined"])
s5s = simple_sheet("Assumptions and Open Items", ["Type", "Ref", "Class / table", "Item", "Action needed"], [24, 8, 46, 100, 50], s5, freeze="A2")
TF = {"Assumption": fill("DDEBF7"), "Class to verify": fill("F8CBAD"), "Low-confidence row": fill("FFEB9C"), "Question for the customer": fill("E2EFDA")}
for i, row in enumerate(s5, 2): s5s.cell(i, 1).fill = TF[row[0]]

wb.save(OUT)

# ------------------------------------------------------------ report
print("classes", len(RECS), "relationships", len(rel_rows), "attributes", len(attr_rows), "open items", len(s5))
print("confidence", Counter(r["conf"] for r in RECS))
print("context", Counter(r["cells"][0] for r in RECS))
print("unused attrs", [a for a in ATTR if not ATTR_USE[a]])

# ------------------------------------------------------------ JSON export for the site
if len(sys.argv) > 2:
    import json
    keys = ["ctx","domain","cat","label","table","parent","shipped","dep","principal","source",
            "req","rec","own","life","key","ident","up","down","host","trace","orphan","stale","dup",
            "audit","csdm","cert","gate","notes","conf"]
    data = dict(
        classes=[dict(zip(keys, rec["cells"]), batch=rec["r"]["batch_title"], p=rec["r"]["parent"], desc=DESC[rec["r"]["table"]]) for rec in RECS],
        rels=[r[1:3] + [r[4]] + r[5:] for r in rel_rows],
        attrs={a[0]: a[1:5] for a in attr_rows},
        patterns=PATTERNS)
    json.dump(data, open(sys.argv[2], "w"), separators=(",", ":"))
    print("json bytes", len(json.dumps(data, separators=(",", ":"))))
