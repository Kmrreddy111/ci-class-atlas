# Data model for the CMDB 3C workbook: attributes, profiles, class inventory.

# ---------------------------------------------------------------- attributes
# name: (label, defined on, type, why it matters)
ATTR = {
 "name": ("Name", "cmdb_ci", "String", "Display value and a common identifier entry; naming standard drives matching and reporting."),
 "sys_class_name": ("Class", "cmdb_ci", "System class name", "Wrong class means wrong identification rule, wrong health rules and wrong CSDM layer."),
 "short_description": ("Description", "cmdb_ci", "String", "Tells a reviewer what the CI is for when the name is not self-explanatory."),
 "number": ("Number", "cmdb_ci_service / cmdb_ci_business_app", "String (auto-number)", "Stable reference used in portfolio and integration records."),
 "operational_status": ("Operational status", "cmdb_ci", "Integer (choice)", "Legacy status still read by many processes; must agree with life cycle fields."),
 "install_status": ("Install status", "cmdb_ci", "Integer (choice)", "Legacy status used by asset synchronisation and many filters."),
 "life_cycle_stage": ("Life Cycle Stage", "cmdb_ci", "Reference (life_cycle_stage)", "CSDM standard life cycle; drives what may be selected on tasks."),
 "life_cycle_stage_status": ("Life Cycle Stage Status", "cmdb_ci", "Reference (life_cycle_stage_status)", "CSDM standard status within the stage (for example In Use, Retired)."),
 "owned_by": ("Owned by", "cmdb_ci", "Reference (sys_user)", "Accountable owner; approver for certification and service changes."),
 "managed_by": ("Managed by", "cmdb_ci", "Reference (sys_user)", "Named individual responsible for day-to-day management."),
 "managed_by_group": ("Managed by group", "cmdb_ci", "Reference (sys_user_group)", "Group accountable for the CI record and its data quality."),
 "support_group": ("Support group", "cmdb_ci", "Reference (sys_user_group)", "Drives incident assignment and on-call routing."),
 "assignment_group": ("Change Group", "cmdb_ci", "Reference (sys_user_group)", "Group that implements changes on the CI."),
 "change_control": ("Approval group", "cmdb_ci", "Reference (sys_user_group)", "Group that approves changes affecting the CI."),
 "assigned_to": ("Assigned to", "cmdb_ci", "Reference (sys_user)", "User of the device; carries the business context for end-user CIs."),
 "company": ("Company", "cmdb_ci", "Reference (core_company)", "Legal entity or customer that owns the CI; needed for multi-entity reporting."),
 "location": ("Location", "cmdb_ci", "Reference (cmn_location)", "Physical placement; needed for field support and site impact."),
 "environment": ("Environment", "cmdb_ci", "String (choice)", "Separates production from non-production for change risk and impact."),
 "serial_number": ("Serial number", "cmdb_ci", "String", "Primary hardware identifier; first entries of the Hardware identification rule."),
 "asset_tag": ("Asset tag", "cmdb_ci", "String", "Links the physical label to the record."),
 "asset": ("Asset", "cmdb_ci", "Reference (alm_asset)", "Financial and contractual record for the CI."),
 "model_id": ("Model ID", "cmdb_ci", "Reference (cmdb_model)", "Normalised product model; drives life cycle and asset class."),
 "manufacturer": ("Manufacturer", "cmdb_ci", "Reference (core_company)", "Vendor for support and end-of-life tracking."),
 "ip_address": ("IP Address", "cmdb_ci", "IP address", "Management address used by Discovery and by the network adapter identifier lookup."),
 "mac_address": ("MAC Address", "cmdb_ci", "String", "Used with IP address in the network adapter identifier lookup."),
 "fqdn": ("Fully qualified domain name", "cmdb_ci", "String", "Unambiguous host identity across domains."),
 "dns_domain": ("DNS Domain", "cmdb_ci", "String", "Distinguishes hosts with the same short name."),
 "discovery_source": ("Discovery source", "cmdb_ci", "String (choice)", "Shows which source last wrote the CI; required for reconciliation rules."),
 "last_discovered": ("Most recent discovery", "cmdb_ci", "Date/time", "Basis for staleness on discovered classes."),
 "attested_date": ("Attested date", "cmdb_ci", "Date/time", "Basis for staleness on manually maintained classes."),
 "virtual": ("Is Virtual", "cmdb_ci_hardware", "True/False", "Decides which downstream relationship is mandatory (VM instance or rack)."),
 "os": ("Operating System", "cmdb_ci_computer", "String (choice)", "Needed for patching scope, vulnerability matching and class correctness."),
 "os_version": ("OS Version", "cmdb_ci_computer", "String", "End-of-support tracking."),
 "os_domain": ("OS Domain", "cmdb_ci_computer", "String", "Windows domain membership."),
 "cpu_count": ("CPU count", "cmdb_ci_computer", "Integer", "Capacity and licence calculations."),
 "cpu_core_count": ("CPU core count", "cmdb_ci_computer", "Integer", "Core-based software licensing."),
 "ram": ("RAM (MB)", "cmdb_ci_computer", "Integer", "Capacity planning."),
 "disk_space": ("Disk space (GB)", "cmdb_ci_computer", "Decimal", "Capacity planning."),
 "chassis_type": ("Chassis type", "cmdb_ci_computer", "String", "Separates laptops, desktops, blades and rack servers."),
 "host_name": ("Host name", "cmdb_ci_server", "String", "Server host name as reported by the operating system."),
 "classification": ("Classification", "cmdb_ci_server", "String (choice)", "Production / development / UAT marking at server level."),
 "used_for": ("Used for", "cmdb_ci_server / cmdb_ci_service", "String (choice)", "Purpose of the server or service (Production, Staging, QA...)."),
 "firmware_version": ("Firmware version", "cmdb_ci_netgear", "String", "Vulnerability and upgrade planning for network devices."),
 "device_type": ("Device type", "cmdb_ci_netgear", "String", "Functional role of the network device."),
 "version": ("Version", "cmdb_ci_appl / cmdb_ci_service", "String", "Software or service version for support and vulnerability matching."),
 "install_directory": ("Install directory", "cmdb_ci_appl", "String", "Separates several installs of the same product on one host."),
 "tcp_port": ("TCP port(s)", "cmdb_ci_appl", "String", "Listening port; used in identification and service mapping connections."),
 "running_process_command": ("Running process command", "cmdb_ci_appl", "String", "Process signature used to classify and identify the application."),
 "running_process_key_parameters": ("Running process key parameters", "cmdb_ci_appl", "String", "Distinguishes instances of the same process on one host."),
 "config_file": ("Configuration file", "cmdb_ci_appl", "String", "Path Discovery uses to read application configuration."),
 "instance_name": ("Instance name", "cmdb_ci_db_mssql_instance", "String", "Named SQL Server instance; part of its identification."),
 "sid": ("SID", "cmdb_ci_db_ora_instance", "String", "Oracle system identifier; part of its identification."),
 "database_instance": ("Database instance", "cmdb_ci_database", "Reference (cmdb_ci_db_instance)", "Parent instance through which a catalog inherits its context."),
 "busines_criticality": ("Business criticality", "cmdb_ci_service", "String (choice)", "Priority and impact weighting for the service (column name is spelled this way in the platform)."),
 "service_classification": ("Service classification", "cmdb_ci_service", "String (choice)", "Separates Business Service, Technical Service, Application Service and offerings."),
 "parent": ("Parent", "cmdb_ci_service", "Reference (cmdb_ci_service)", "Links an offering to the service it belongs to."),
 "cmdb_group": ("CMDB Group", "cmdb_ci_query_based_service", "Reference (cmdb_group)", "Saved query that populates the Dynamic CI Group."),
 "populator_status": ("Populator status", "cmdb_ci_service_calculated", "String (choice)", "Shows whether the calculated service population succeeded."),
 "service_populator": ("Service populator", "cmdb_ci_service_calculated", "Reference", "Population method used for the calculated service."),
 "application_type": ("Application type", "cmdb_ci_business_app", "String (choice)", "COTS, homegrown or SaaS; drives rationalisation decisions."),
 "architecture_type": ("Architecture type", "cmdb_ci_business_app", "String (choice)", "Architecture style for technology risk assessment."),
 "install_type": ("Install type", "cmdb_ci_business_app", "String (choice)", "On-premises or cloud; decides which infrastructure pattern applies."),
 "platform": ("Platform", "cmdb_ci_business_app", "String (choice)", "Platform the application is built on."),
 "technology_stack": ("Technology stack", "cmdb_ci_business_app", "String", "Technology risk and skills planning."),
 "user_base": ("User base", "cmdb_ci_business_app", "String (choice)", "Scale of impact when the application is unavailable."),
 "business_unit": ("Business unit", "cmdb_ci_business_app", "Reference (business_unit)", "Owning business unit."),
 "it_application_owner": ("IT application owner", "cmdb_ci_business_app", "Reference (sys_user)", "IT-side owner who certifies the record."),
 "account_id": ("Account Id", "cmdb_ci_cloud_service_account", "String", "Cloud account / subscription / project identifier; identification entry."),
 "datacenter_type": ("Datacenter type", "cmdb_ci_cloud_service_account", "String", "Cloud provider datacenter class for the account."),
 "region": ("Region", "cmdb_ci_logical_datacenter", "String", "Cloud region; part of logical datacenter identification."),
 "object_id": ("Object ID", "cmdb_ci_vm_object and cloud resource classes", "String", "Provider resource identifier; primary identification entry for cloud and virtual resources."),
 "state": ("State", "cmdb_ci_vm_instance", "String (choice)", "Power state; terminated instances must be retired."),
 "cpus": ("CPUs", "cmdb_ci_vm_instance", "Integer", "Allocated virtual CPUs."),
 "memory": ("Memory (MB)", "cmdb_ci_vm_instance", "Integer", "Allocated memory."),
 "disks_size": ("Disks size (GB)", "cmdb_ci_vm_instance", "Integer", "Allocated storage."),
 "nics": ("Network adapters", "cmdb_ci_vm_instance", "Integer", "Number of virtual network adapters."),
 "fingerprint": ("Fingerprint", "cmdb_ci_certificate", "String", "Unique certificate hash; identification entry."),
 "subject_common_name": ("Subject common name", "cmdb_ci_certificate", "String", "What the certificate secures."),
 "issuer_common_name": ("Issuer common name", "cmdb_ci_certificate", "String", "Issuing authority."),
 "valid_from": ("Valid from", "cmdb_ci_certificate", "Date/time", "Start of validity."),
 "valid_to": ("Valid to", "cmdb_ci_certificate", "Date/time", "Expiry date; drives renewal."),
 "netmask": ("Netmask", "cmdb_ci_network_adapter / cmdb_ci_ip_address", "String", "Subnet membership."),
 "nic": ("Nic", "cmdb_ci_ip_address", "Reference (cmdb_ci_network_adapter)", "Adapter that owns the address."),
 "cmdb_ci": ("Configuration Item", "cmdb_ci_network_adapter", "Reference (cmdb_ci)", "Parent device through which the component inherits context."),
 "subnet": ("Subnet", "cmdb_ci_ip_network", "String", "Network address range."),
 "load_balancer": ("Load balancer", "cmdb_ci_lb_service / cmdb_ci_lb_pool", "Reference (cmdb_ci_lb)", "Device that hosts the virtual server or pool."),
 "cluster": ("Cluster", "cmdb_ci_cluster_node / cmdb_ci_cluster_resource / cmdb_ci_cluster_vip", "Reference (cmdb_ci_cluster)", "Cluster the component belongs to."),
 "server": ("Server", "cmdb_ci_cluster_node", "Reference (cmdb_ci_server)", "Host that backs the cluster node."),
 "size_bytes": ("Size bytes", "cmdb_ci_storage_volume / cmdb_ci_file_system / cmdb_ci_disk", "Integer", "Capacity."),
 "free_space_bytes": ("Free space bytes", "cmdb_ci_file_system", "Integer", "Capacity headroom."),
 "mount_point": ("Mount point", "cmdb_ci_file_system", "String", "Where the file system is mounted."),
 "computer": ("Computer", "cmdb_ci_file_system / cmdb_ci_disk", "Reference (cmdb_ci_computer)", "Host through which the component inherits context."),
 "rack_units": ("Rack units", "cmdb_ci_rack", "Integer", "Rack capacity."),
}

# ---------------------------------------------------------------- helpers
def R(parent, rtype, child, kind, mand="M", by="Discovery"):
    return (parent, rtype, child, kind, mand, by)

S = "SELF"
DEP, USE, RUN, HOST, VIRT, CONT, CONS = ("Depends on::Used by", "Uses::Used by", "Runs on::Runs",
    "Hosted on::Hosts", "Virtualized by::Virtualizes", "Contains::Contained by", "Consumes::Consumed by")
REG, MEM, LOC, PROV = "Registered on::Has registered", "Members::Member of", "Located in::Houses", "Provides::Provided by"
ASSOC = "Service CI association (svc_ci_assoc)"
REFP = "Reference field: parent"

LIFE = ["life_cycle_stage", "life_cycle_stage_status", "operational_status", "install_status"]
OWN_SVC = ["owned_by", "managed_by_group", "support_group", "change_control"]
OWN_INF = ["managed_by_group", "support_group", "change_control"]

TOP = "Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> "
SRV_TAIL = ("Server -> Virtualized by::Virtualizes -> VM Instance -> Registered on::Has registered -> ESX Server "
            "(cloud: Hosted on::Hosts -> Logical Datacenter -> Hosted on::Hosts -> Cloud Service Account; "
            "physical: Located in::Houses -> Rack -> Computer Room -> Data Center)")
CLOUD_TAIL = "Hosted on::Hosts -> Logical Datacenter -> Hosted on::Hosts -> Cloud Service Account"

BASE = dict(
    req=["name", "operational_status", "discovery_source", "last_discovered"],
    rec=["short_description", "environment"], own=OWN_INF, life=LIFE, key=[],
    ident="Verify in instance: identifier entries for this class in CI Class Manager.",
    rels=[], up_text="", down_text="", host="Not applicable (independent class)",
    trace="", dep="Independent", source="Discovery",
    orphan="CI has no upstream link to a Service Instance and no downstream hosting relationship.",
    stale="30 days without a discovery update (last_discovered). Refreshed by the scheduled Discovery or Service Graph Connector run. Platform default is 60 days.",
    dup="Discovery / Service Graph Connector is authoritative for technical attributes. Manual and import sources must pass through IRE with lower reconciliation priority.",
    audit="Ownership groups populated and active; life cycle values valid; discovery_source populated; mandatory relationships present.",
    csdm="Infrastructure CI in Service Delivery: reachable from a Service Instance (relationship or svc_ci_assoc) and owned through a Technology Management Offering / Dynamic CI Group.",
    cert="Managed-by group lead; quarterly",
    gate="Pass if required attributes are populated, the CI is uniquely identified, and the upstream and downstream relationships exist. Fail otherwise.",
    note="", conf="Medium")

def prof(base=None, **kw):
    d = dict(BASE if base is None else P[base])
    d.update(kw)
    return d

P = {}

# ---------------------------------------------------------------- business context
MANUAL_STALE = "365 days without attestation (attested_date). Refreshed by owner review / data certification. Not discovered."
P["bizapp"] = prof(
    req=["name", "short_description", "application_type", "install_type", "business_unit", "it_application_owner", "owned_by", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["architecture_type", "platform", "technology_stack", "user_base", "Verify in instance: criticality and data classification fields provided by APM"],
    own=["owned_by", "it_application_owner", "managed_by_group", "support_group"],
    life=["life_cycle_stage", "life_cycle_stage_status", "install_status"],
    key=["number", "application_type", "install_type", "business_unit"],
    ident="Independent. Match on name (verify the active identifier entry in CI Class Manager); number is system-generated. Source of truth is the application portfolio (APM / EA tool).",
    rels=[R(S, CONS, "cmdb_ci_service_auto", "down", "M", "Manual / APM"),
          R(S, PROV, "cmdb_ci_business_capability", "lat", "O", "Manual / APM")],
    up_text="None: Business Application is the top of the trace. Anchor it laterally to Business Capability and Information Object.",
    trace="{L} -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> Application / Database Instance -> Runs on::Runs -> " + SRV_TAIL,
    source="Manual / APM / EA tool import",
    orphan="Operational Business Application with no Consumes::Consumed by relationship to any Service Instance.",
    stale=MANUAL_STALE,
    dup="High risk when several portfolio lists exist (EA tool, spreadsheets, APM). Portfolio tool is authoritative; match on name and number before import.",
    audit="owned_by and it_application_owner are active users; life cycle valid; at least one production Service Instance linked; no direct relationship to infrastructure CIs.",
    csdm="Design & Planning record: linked to Service Instances through Consumes::Consumed by, never directly to servers; not used as the affected CI on incident or change.",
    cert="IT application owner; every 6 months",
    gate="Pass if owner, type, life cycle and at least one Service Instance are present. Fail if it relates directly to infrastructure.",
    conf="High")

P["design"] = prof(
    req=["name", "short_description", "owned_by", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["managed_by_group", "Verify in instance: class-specific fields"],
    own=["owned_by", "managed_by_group"], life=["life_cycle_stage", "life_cycle_stage_status"],
    key=["Verify in instance: class-specific key fields"],
    ident="Independent. Match on name (verify identifier entry). Manually maintained.",
    up_text="None: business-context record at the top of the model.",
    down_text="Verify in instance: link to Business Application.",
    trace="{L} -> Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> infrastructure CIs",
    source="Manual / APM / EA tool import",
    orphan="Record is not linked to any Business Application.",
    stale=MANUAL_STALE, dup="Low volume, manually curated. Enterprise architecture is authoritative.",
    audit="Owner populated and active; life cycle valid; linked to at least one Business Application.",
    csdm="Business-context record: describes what the business does or holds; never related directly to infrastructure CIs.",
    cert="Enterprise architecture / business owner; yearly",
    gate="Pass if owner and at least one Business Application link exist.")

P["svc_base"] = prof(
    req=["name", "owned_by", "service_classification", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["busines_criticality", "short_description"], own=OWN_SVC, key=["number", "service_classification"],
    ident="Independent. Match on name; number is system-generated.",
    up_text="Not applicable: abstract parent. Use Business Service, Technology Management Service, Service Offering or Service Instance.",
    down_text="Not applicable: abstract parent.",
    trace="Abstract parent of all service classes. A record here cannot be traced; reclassify it.",
    source="Should not be populated directly",
    orphan="Any record whose class is exactly cmdb_ci_service.",
    stale=MANUAL_STALE, dup="Legacy service records often duplicate Business Services or Service Instances. Reclassify, then merge.",
    audit="Count of records with sys_class_name = cmdb_ci_service is zero.",
    csdm="CSDM uses the child classes. Records left in the base class are a CSDM 'crawl' gap.",
    cert="Service portfolio manager; yearly",
    gate="Fail: reclassify to the correct service class before acceptance.", conf="High")

P["bizservice"] = prof(
    req=["name", "short_description", "owned_by", "busines_criticality", "service_classification", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["managed_by_group", "support_group", "Verify in instance: portfolio / taxonomy fields"],
    own=OWN_SVC, life=["life_cycle_stage", "life_cycle_stage_status", "operational_status"],
    key=["number", "service_classification", "busines_criticality"],
    ident="Independent. Match on name; number is system-generated. Service portfolio is authoritative.",
    rels=[R(S, REFP, "service_offering", "down", "M", "Manual / Service Portfolio Management")],
    up_text="None mandatory. Optional alignment to Business Capability and a service portfolio / taxonomy node.",
    trace="{L} -> parent (reference) -> Business Service Offering -> Depends on::Used by -> Service Instance -> Depends on::Used by -> infrastructure CIs",
    source="Manual / Service Portfolio Management",
    orphan="Operational Business Service with no Service Offering.",
    stale=MANUAL_STALE, dup="Service catalogue and portfolio lists overlap. Portfolio owner decides the master list.",
    audit="service_classification = Business Service; owner active; at least one offering; no direct relationship to infrastructure CIs.",
    csdm="Service Consumption record: consumers subscribe to its offerings; technical dependency is expressed only from the offering to Service Instances.",
    cert="Business service owner; yearly",
    gate="Pass if owner, criticality and at least one offering exist.", conf="High")

P["techservice"] = prof("bizservice",
    rels=[R(S, REFP, "service_offering", "down", "M", "Manual")],
    up_text="None: top of the technology-management branch.",
    trace="{L} -> parent (reference) -> Technology Management Offering -> Contains::Contained by -> Dynamic CI Group -> svc_ci_assoc -> infrastructure CIs",
    source="Manual", orphan="Operational Technology Management Service with no Technology Management Offering.",
    audit="service_classification = Technical Service; owner active; at least one offering with support and approval groups.",
    csdm="Service Delivery record (former Technical Service): groups the offerings through which infrastructure teams own CIs.",
    cert="Technology service owner; yearly")

P["offering"] = prof("bizservice",
    req=["name", "parent", "service_classification", "owned_by", "support_group", "change_control", "managed_by_group", "busines_criticality", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["short_description", "Verify in instance: commitments and subscription records (service_offering_commitment, service_subscribe_*)"],
    key=["parent", "service_classification"],
    ident="Independent. Match on name within parent service (verify identifier entry).",
    rels=[R("cmdb_ci_service_business", REFP, S, "up", "Mandatory (Business Service Offering)", "Manual"),
          R("cmdb_ci_service_technical", REFP, S, "up", "Mandatory (Technology Management Offering)", "Manual"),
          R(S, DEP, "cmdb_ci_service_auto", "down", "Mandatory (Business Service Offering)", "Manual"),
          R(S, CONT, "cmdb_ci_query_based_service", "down", "Mandatory (Technology Management Offering)", "Manual")],
    trace="Business Service / Technology Management Service -> parent (reference) -> {L} -> Depends on::Used by -> Service Instance (or Contains::Contained by -> Dynamic CI Group) -> infrastructure CIs",
    source="Manual / Service Portfolio Management",
    orphan="Offering with empty parent, or with neither a Service Instance nor a Dynamic CI Group below it.",
    audit="parent populated; support_group and change_control populated; classification matches parent service type.",
    csdm="Offering is where support, approval and commitments live. Business Service Offering depends on Service Instances; Technology Management Offering contains Dynamic CI Groups.",
    cert="Offering owner; every 6 months",
    gate="Pass if parent, support group, approval group and one downstream link exist.",
    note="Business Service Offering belongs to Service Consumption; Technology Management Offering belongs to Service Delivery. Verify the table name and classification values in the instance.")

# ---------------------------------------------------------------- application context
P["svc_instance"] = prof(
    req=["name", "environment", "busines_criticality", "service_classification", "owned_by", "managed_by_group", "support_group", "change_control", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["version", "used_for", "short_description", "attested_date"],
    own=OWN_SVC, key=["number", "environment", "used_for", "busines_criticality"],
    ident="Independent. Match on name (convention: <Business Application> - <Environment>); number is system-generated. Enforce one record per application and environment.",
    rels=[R("cmdb_ci_business_app", CONS, S, "up", "M", "Manual / APM"),
          R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_appl", "down", "M", "Manual / Service Mapping")],
    trace=TOP.replace("Service Instance", "{L}") + "Application / Database Instance -> Runs on::Runs -> " + SRV_TAIL,
    source="Manual / Service Mapping",
    orphan="Operational Service Instance with no Business Application above it, or with no CIs below it (no Depends on relationship and empty svc_ci_assoc).",
    stale="60 days without recalculation or update; 180 days without attestation for manually built services.",
    dup="Created by several routes (manual, Service Mapping, tags, connectors). One Service Instance per application and environment; merge by name + environment.",
    audit="Business Application and offering linked; environment and criticality populated; support and approval groups populated; at least one CI in the service.",
    csdm="Service Delivery record (former Application Service): the only bridge between business context and infrastructure. Use the most specific Service Instance type.",
    cert="Service Instance owner; every 6 months",
    gate="Pass if Business Application above, offering linked, environment set, and at least one infrastructure CI below.", conf="High")

P["dcg"] = prof("svc_instance",
    req=["name", "cmdb_group", "owned_by", "managed_by_group", "support_group", "change_control", "life_cycle_stage", "life_cycle_stage_status"],
    rec=["short_description"], key=["cmdb_group"],
    ident="Independent. Match on name; one group per CMDB Group query.",
    rels=[R("service_offering", CONT, S, "up", "M", "Manual"),
          R(S, ASSOC, "cmdb_ci", "down", "M", "CMDB Group saved query")],
    trace="Technology Management Service -> parent (reference) -> Technology Management Offering -> Contains::Contained by -> {L} -> svc_ci_assoc -> member infrastructure CIs",
    source="Manual (CMDB Group query)",
    orphan="Dynamic CI Group not contained by any Technology Management Offering, or whose CMDB Group returns no CIs.",
    stale="60 days without recalculation.",
    dup="Overlapping queries put one CI in several groups. Acceptable only when intended; review overlap yearly.",
    audit="cmdb_group populated and query returns CIs; contained by exactly one Technology Management Offering.",
    csdm="Mechanism that gives every infrastructure CI an owning offering (support, approval) without per-CI relationships.",
    gate="Pass if a query is attached, it returns CIs, and an offering contains the group.", conf="Medium")

P["app_logical"] = prof(
    req=["name", "operational_status"], rec=["short_description", "environment"],
    key=["Verify in instance: class-specific identifiers"],
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Manual / Service Mapping")],
    down_text="Verify in instance: hosting relationship to the application or server that implements it.",
    trace=TOP + "{L} -> (hosting relationship, verify) -> Application / Server -> infrastructure",
    source="Discovery pattern / integration / manual",
    orphan="Not referenced by any Service Instance.",
    csdm="Logical application-layer CI: must be part of a Service Instance; ownership through the Service Instance or a Technology Management Offering.",
    cert="Service Instance owner; every 6 months", conf="Low")

# ---------------------------------------------------------------- infrastructure: applications
P["appl"] = prof(
    req=["name", "sys_class_name", "version", "operational_status", "discovery_source", "last_discovered"],
    rec=["install_directory", "tcp_port", "config_file", "running_process_command", "environment", "short_description"],
    key=["version", "install_directory", "tcp_port", "running_process_command", "running_process_key_parameters"],
    ident="Dependent class. Identifier entries combine sys_class_name with class-specific attributes (for example install_directory, tcp_port, running_process_command + running_process_key_parameters) within the host. Verify the entries per class.",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Service Mapping / manual"),
          R(S, RUN, "cmdb_ci_server", "down", "M", "Discovery")],
    host="Hosting rule: {L} Runs on::Runs Hardware [cmdb_ci_hardware]. IRE rejects the CI without its host.",
    trace=TOP + "{L} -> Runs on::Runs -> " + SRV_TAIL,
    dep="Dependent", source="Discovery pattern (horizontal) / Service Mapping / Agent Client Collector",
    orphan="Application with no Runs on::Runs host, or not part of any Service Instance.",
    audit="Class is specific (not Generic Application where a product class exists); version populated; host present; member of a Service Instance.",
    gate="Pass if discovered on a known host, class is specific, and it belongs to a Service Instance.", conf="High")

P["db_instance"] = prof("appl",
    req=["name", "sys_class_name", "version", "tcp_port", "operational_status", "discovery_source", "last_discovered"],
    rec=["install_directory", "environment", "short_description"],
    key=["version", "tcp_port", "Verify in instance: engine-specific identifier"],
    ident="Dependent class. Identifier entries use the engine-specific instance identifier (for example instance_name for SQL Server, sid for Oracle, tcp_port for others) within the host. Verify per class.",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Service Mapping / manual"),
          R("cmdb_ci_data_service_instance", DEP, S, "up", "O", "Manual"),
          R(S, RUN, "cmdb_ci_server", "down", "M", "Discovery"),
          R(S, CONT, "cmdb_ci_db_catalog", "lat", "O", "Discovery")],
    trace=TOP + "{L} -> Runs on::Runs -> " + SRV_TAIL,
    audit="Engine version populated and supported; host present; member of a Service Instance or Data Service Instance; catalogs linked.",
    gate="Pass if discovered on a known host with version and port, and it belongs to a Service Instance.")

P["component"] = prof(
    req=["name", "operational_status"], rec=["short_description"],
    own=["Inherited from the parent CI"], life=["operational_status", "install_status"],
    key=["Verify in instance: class-specific identifiers"],
    ident="Dependent component. Identified within its parent CI (containment rule or reference field). Verify identifier entries.",
    down_text="None: leaf component. Context is inherited through the parent CI.",
    host="Dependent on the parent CI named in the upstream column; cannot exist without it.",
    trace="Business Application -> Service Instance -> ... -> {V} -> {L} (component; inherits all three contexts from {V})",
    dep="Dependent", orphan="Component with no parent CI.",
    stale="Follows the parent CI: 30 days without discovery update.",
    dup="Low risk when the parent is unique; duplicates here usually signal a duplicate parent.",
    audit="Parent CI present and operational; component retired when the parent is retired.",
    csdm="Component class: carries no service relationship of its own. Do not select it on tasks; use the parent CI.",
    cert="Certified with the parent CI",
    gate="Pass if the parent CI exists and passes its own gate.", conf="Medium")

P["db_catalog"] = prof("component",
    req=["name", "database_instance", "operational_status"], key=["database_instance"],
    ident="Dependent. Identified by name within its Database Instance.",
    conf="Medium")

P["certificate"] = prof(
    req=["name", "fingerprint", "subject_common_name", "issuer_common_name", "valid_from", "valid_to"],
    rec=["owned_by", "environment"], own=["owned_by", "managed_by_group", "support_group"],
    key=["fingerprint", "valid_to", "subject_common_name"],
    ident="Independent. Match on fingerprint.",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Manual / Certificate Inventory and Management")],
    down_text="Verify in instance: link from the certificate to the server or URL where it is installed (Certificate Inventory and Management).",
    trace=TOP + "{L} -> (installed on, verify) -> Server / Load Balancer Service",
    source="Certificate discovery / import",
    orphan="Certificate not linked to any host, URL or Service Instance.",
    stale="30 days without discovery update; expired certificates retired after valid_to.",
    audit="valid_to in the future or renewal task open; owner populated; installed-on link present.",
    gate="Pass if fingerprint, expiry, owner and installed-on link are present.", conf="Medium")

# ---------------------------------------------------------------- infrastructure: compute
HW_REQ = ["name", "serial_number", "model_id", "manufacturer", "ip_address", "location", "operational_status", "discovery_source", "last_discovered"]
HW_REC = ["asset", "asset_tag", "fqdn", "dns_domain", "mac_address", "company", "environment", "virtual"]
HW_KEY = ["serial_number", "model_id", "ip_address", "virtual"]
SRV_REQ = HW_REQ + ["os", "os_version", "used_for"]
SRV_REC = HW_REC + ["cpu_count", "cpu_core_count", "ram", "disk_space", "os_domain", "chassis_type", "host_name", "classification"]
SRV_KEY = HW_KEY + ["os", "os_version", "cpu_core_count", "ram", "host_name", "used_for"]
HW_IDENT = ("Independent. Hardware Rule, in priority order: (1) Serial Number table lookup [cmdb_serial_number]: serial_number + serial_number_type; "
            "(2) serial_number; (3) name; (4) Network Adapter lookup [cmdb_ci_network_adapter]: ip_address + mac_address.")
HW_DUP = "Cloned VMs, re-imaged hosts and blank serial numbers cause duplicates. Discovery is authoritative; imports must supply serial number and pass through IRE."

P["server"] = prof(
    req=HW_REQ, rec=HW_REC, key=HW_KEY, ident=HW_IDENT,
    rels=[R("cmdb_ci_appl", RUN, S, "up", "M", "Discovery"),
          R("cmdb_ci_service_auto", DEP, S, "up", "O", "Service Mapping / manual (or svc_ci_assoc membership)"),
          R(S, VIRT, "cmdb_ci_vm_instance", "down", "Mandatory (virtual servers)", "Discovery / cloud discovery"),
          R(S, LOC, "cmdb_ci_rack", "down", "Mandatory (physical servers)", "Manual / DCIM import")],
    trace=TOP + "Application -> Runs on::Runs -> {L} -> Virtualized by::Virtualizes -> VM Instance -> Registered on::Has registered -> ESX Server "
          "(cloud: " + CLOUD_TAIL + "; physical: Located in::Houses -> Rack -> Computer Room -> Data Center)",
    source="Discovery (IP-based) / Agent Client Collector / Service Graph Connector",
    orphan="Server that runs no application and belongs to no Service Instance; or virtual server with no VM Instance; or physical server with no location.",
    dup=HW_DUP,
    audit="Serial number, OS and version populated; OS in support; virtual flag agrees with relationships; support group populated; member of a Service Instance or Dynamic CI Group.",
    gate="Pass if uniquely identified by serial number, OS known, owner group set, and both upstream (application / service) and downstream (VM or rack) links exist.",
    conf="High")

P["hypervisor"] = prof("server", req=SRV_REQ, rec=SRV_REC, key=SRV_KEY,
    rels=[R("cmdb_ci_vm_instance", REG, S, "up", "M", "Discovery (vCenter / hypervisor)"),
          R(S, LOC, "cmdb_ci_rack", "down", "M", "Manual / DCIM import"),
          R("cmdb_ci_vcenter_cluster", MEM, S, "lat", "O", "Discovery (vCenter)")],
    trace=TOP + "Application -> Runs on::Runs -> Server -> Virtualized by::Virtualizes -> VM Instance -> Registered on::Has registered -> {L} -> Located in::Houses -> Rack -> Computer Room -> Data Center",
    orphan="Hypervisor host with no registered VM Instances, or with no physical placement.",
    audit="Serial number and version populated; cluster membership present; rack and location populated.",
    gate="Pass if uniquely identified, placed in a rack, and VM Instances are registered on it.", conf="Medium")

P["chassis"] = prof("server",
    rels=[R(S, CONT, "cmdb_ci_server", "up", "M", "Discovery"),
          R(S, LOC, "cmdb_ci_rack", "down", "M", "Manual / DCIM import")],
    trace=TOP + "Application -> Runs on::Runs -> Server -> Contains::Contained by (child of) -> {L} -> Located in::Houses -> Rack -> Computer Room -> Data Center",
    orphan="Enclosure that contains no servers, or has no physical placement.",
    audit="Serial number and model populated; rack and location populated; contained servers present.",
    gate="Pass if uniquely identified, placed in a rack, and it contains at least one server.", conf="Medium")

P["cluster"] = prof(
    req=["name", "operational_status", "discovery_source", "last_discovered"], rec=["short_description", "environment", "ip_address"],
    key=["Verify in instance: cluster identifier fields"],
    ident="Independent. Verify identifier entries (commonly name, with cluster identifier where present).",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Service Mapping / manual"),
          R("cmdb_ci_cluster_node", "Reference field: cluster", S, "down", "M", "Discovery")],
    trace=TOP + "Application -> (clustered on) -> {L} -> Cluster Node (cluster reference) -> Server (server reference) -> " + SRV_TAIL.split("Server -> ", 1)[1],
    orphan="Cluster with no nodes.",
    audit="At least two nodes for a production cluster; nodes resolve to operational servers.",
    gate="Pass if nodes exist and each node resolves to a server that passes its own gate.")

# ---------------------------------------------------------------- infrastructure: network
P["netgear"] = prof("server",
    req=HW_REQ + ["firmware_version"], rec=HW_REC + ["device_type"], key=["serial_number", "model_id", "ip_address", "firmware_version", "device_type"],
    rels=[R("cmdb_ci_network_service_instance", DEP, S, "up", "M", "Manual"),
          R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"),
          R(S, LOC, "cmdb_ci_rack", "down", "Mandatory (data center devices)", "Manual / DCIM import")],
    trace="Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> Network Service Instance -> Depends on::Used by -> {L} -> Located in::Houses -> Rack -> Computer Room -> Data Center (site devices: location)",
    source="Discovery (SNMP) / network controller integration",
    orphan="Network device that belongs to no Network Service Instance or Dynamic CI Group, or has no location.",
    audit="Serial number, model and firmware populated; firmware in support; location populated; member of a Network Service Instance or Dynamic CI Group.",
    gate="Pass if uniquely identified, firmware known, location set, and it is a member of a network service or Dynamic CI Group.", conf="High")

P["lb_logical"] = prof(
    req=["name", "ip_address", "load_balancer", "operational_status"], rec=["short_description", "environment"],
    key=["ip_address", "load_balancer"],
    ident="Dependent. Identified by name (and address / port) within its load balancer. Verify identifier entries.",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Service Mapping"),
          R(S, "Reference field: load_balancer", "cmdb_ci_lb", "down", "M", "Discovery")],
    host="Dependent on its Load Balancer [cmdb_ci_lb] through the load_balancer reference.",
    trace=TOP + "{L} -> load_balancer (reference) -> Load Balancer -> Located in::Houses -> Rack -> Data Center",
    dep="Dependent", source="Discovery (load balancer patterns) / Service Mapping",
    orphan="Virtual server or pool with no load balancer, or not used by any Service Instance.",
    audit="Load balancer populated; pool has members; used by a Service Instance.",
    gate="Pass if tied to a load balancer and used by a Service Instance.")

P["net_logical"] = prof(
    req=["name", "operational_status"], rec=["short_description", "environment"],
    key=["Verify in instance: class-specific identifiers"],
    rels=[R("cmdb_ci_network_service_instance", DEP, S, "up", "O", "Manual")],
    down_text="Verify in instance: relationship to the network device or provider that realises it.",
    trace="Business Application -> Service Instance -> Network Service Instance -> Depends on::Used by -> {L} -> network device / provider (verify)",
    source="Discovery / IPAM or DNS integration / manual",
    orphan="Logical network object not referenced by any device, service or Network Service Instance.",
    csdm="Logical network object: owned through a Network Service Instance or a Technology Management Offering (Dynamic CI Group).",
    conf="Low")

# ---------------------------------------------------------------- infrastructure: storage
P["storage_hw"] = prof("netgear",
    req=HW_REQ, rec=HW_REC + ["Verify in instance: capacity fields"], key=HW_KEY,
    rels=[R("cmdb_ci_data_service_instance", DEP, S, "up", "O", "Manual"),
          R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"),
          R(S, LOC, "cmdb_ci_rack", "down", "M", "Manual / DCIM import")],
    trace="Business Application -> Service Instance -> Server -> (storage volume / file system) -> {L} -> Located in::Houses -> Rack -> Computer Room -> Data Center",
    source="Discovery (SMI-S / CIM / vendor API)",
    orphan="Storage system in no Dynamic CI Group, or with no physical placement.",
    audit="Serial number and model populated; location and rack populated; member of a storage Dynamic CI Group.",
    gate="Pass if uniquely identified, placed in a rack, and owned through a storage offering.", conf="Medium")

# ---------------------------------------------------------------- infrastructure: virtualisation
P["vm"] = prof(
    req=["name", "object_id", "operational_status", "discovery_source", "last_discovered"],
    rec=["short_description", "environment"], key=["object_id"],
    ident="Dependent. Match on object_id within the hosting datacenter (vCenter: object_id with the vCenter instance identifier). Verify identifier entries.",
    rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery / cloud discovery"),
          R(S, REG, "cmdb_ci_esx_server", "down", "Mandatory (on-premises VMware)", "Discovery (vCenter)"),
          R(S, HOST, "cmdb_ci_logical_datacenter", "down", "Mandatory (cloud)", "Cloud discovery / Service Graph Connector")],
    host="Hosting rule: {L} Hosted on::Hosts Logical Datacenter (cloud) or is tied to its vCenter datacenter (on-premises).",
    trace=TOP + "Application -> Runs on::Runs -> Server -> Virtualized by::Virtualizes -> {L} -> Registered on::Has registered -> ESX Server (cloud: " + CLOUD_TAIL + ")",
    dep="Dependent", source="Discovery (vCenter / hypervisor) / cloud discovery / Service Graph Connector",
    orphan="VM Instance with no Server above it (guest not discovered), or with no host / logical datacenter below it.",
    stale="7 days without discovery update for cloud instances; 30 days for on-premises. Terminated instances are retired, not left operational.",
    dup="The same VM can arrive from hypervisor discovery, cloud discovery and a connector. object_id is the key; set reconciliation precedence per attribute.",
    audit="state is not terminated for operational records; Server linked through Virtualized by; host or logical datacenter linked.",
    gate="Pass if object_id is present, a Server is linked above and a host or logical datacenter below.", conf="High")

P["virt_obj"] = prof(
    req=["name", "object_id", "operational_status", "discovery_source", "last_discovered"], rec=["short_description"],
    key=["object_id", "Verify in instance: vCenter reference fields (vcenter_ref, vcenter_uuid)"],
    ident="Dependent. Match on object_id within the managing vCenter / hypervisor manager. Verify identifier entries.",
    rels=[R("cmdb_ci_vcenter_datacenter", CONT, S, "down", "M", "Discovery (vCenter)")],
    up_text="Inherits context from the VM Instances and ESX Servers that use it (verify relationship type in instance).",
    trace="Business Application -> Service Instance -> Application -> Server -> VM Instance -> ESX Server -> {L} -> VMware vCenter Datacenter -> VMware vCenter Instance",
    dep="Dependent", source="Discovery (vCenter / hypervisor manager)",
    orphan="Virtualisation object not attached to a datacenter or manager, or unused by any host or VM.",
    csdm="Platform object: no direct service relationship. Owned through a virtualisation Technology Management Offering (Dynamic CI Group).",
    gate="Pass if tied to its manager / datacenter and owned through a virtualisation offering.")

# ---------------------------------------------------------------- infrastructure: cloud
TAGS = "Note: mandatory tags held as Key Value records [cmdb_key_value] (application, environment, owner, cost centre)"
P["cloud_account"] = prof(
    req=["name", "account_id", "datacenter_type", "operational_status", "discovery_source"],
    rec=["short_description", "environment", "company", "owned_by"],
    own=["owned_by", "managed_by_group", "support_group", "change_control"], key=["account_id", "datacenter_type"],
    ident="Independent. Match on account_id.",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Manual"),
          R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"),
          R("cmdb_ci_logical_datacenter", HOST, S, "down", "M", "Cloud discovery / Service Graph Connector")],
    trace=TOP + "cloud resource -> Hosted on::Hosts -> Logical Datacenter -> Hosted on::Hosts -> {L}",
    source="Cloud discovery / Service Graph Connector (AWS, Azure, GCP)",
    orphan="Account with no logical datacenters hosted on it, or with no owner.",
    stale="7 days without discovery update.",
    dup="One record per account / subscription / project. Duplicates appear when a connector and cloud discovery use different names; account_id is the key.",
    audit="account_id populated; owner and support group populated; environment populated; discovery credentials valid.",
    csdm="Bottom of every cloud trace. Owned by the platform team through a Technology Management Offering; business context comes from the resources and their tags.",
    cert="Cloud platform owner; quarterly",
    gate="Pass if account_id, owner, environment and at least one logical datacenter are present.",
    note="The account is the bottom of the hosting chain. The logical datacenters and resources it hosts are listed as its downstream scope.", conf="High")

P["cloud_dc"] = prof(
    req=["name", "region", "operational_status", "discovery_source", "last_discovered"], rec=["short_description"],
    key=["region"],
    ident="Dependent. Match on region within the Cloud Service Account.",
    rels=[R("cmdb_ci_vm_instance", HOST, S, "up", "M", "Cloud discovery / Service Graph Connector"),
          R(S, HOST, "cmdb_ci_cloud_service_account", "down", "M", "Cloud discovery / Service Graph Connector")],
    host="Hosting rule: {L} Hosted on::Hosts Cloud Service Account [cmdb_ci_cloud_service_account].",
    trace=TOP + "cloud resource -> Hosted on::Hosts -> {L} -> Hosted on::Hosts -> Cloud Service Account",
    dep="Dependent", source="Cloud discovery / Service Graph Connector",
    orphan="Logical datacenter not hosted on a Cloud Service Account.",
    stale="7 days without discovery update.",
    dup="One record per account and region. Low risk when hosted on a unique account.",
    audit="region populated; hosted on exactly one Cloud Service Account.",
    csdm="Represents a cloud region for one account. No direct service relationship; context flows through hosted resources.",
    cert="Cloud platform owner; quarterly",
    gate="Pass if region is set and it is hosted on a Cloud Service Account.", conf="High")

P["cloud_resource"] = prof(
    req=["name", "object_id", "operational_status", "discovery_source", "last_discovered"],
    rec=["short_description", "environment", TAGS], key=["object_id"],
    ident="Dependent. Match on object_id within the Logical Datacenter.",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Tag-based service mapping / manual"),
          R(S, HOST, "cmdb_ci_logical_datacenter", "down", "M", "Cloud discovery / Service Graph Connector")],
    host="Hosting rule: {L} Hosted on::Hosts Logical Datacenter [cmdb_ci_logical_datacenter].",
    trace=TOP + "{L} -> " + CLOUD_TAIL,
    dep="Dependent", source="Cloud discovery / Service Graph Connector (AWS, Azure, GCP)",
    orphan="Resource not hosted on a logical datacenter, or not a member of any Service Instance (usually missing tags).",
    stale="7 days without discovery update. Deleted resources are retired by the connector, not left operational.",
    dup="Connector and cloud discovery can both create the resource. object_id is the key; pick one authoritative source per provider.",
    audit="Mandatory tags present; object_id populated; hosted on a logical datacenter; member of a Service Instance.",
    csdm="Cloud resource: tied to a Service Instance (tag-based) above and to Logical Datacenter and Cloud Service Account below.",
    cert="Service Instance owner (from tags); quarterly",
    gate="Pass if tagged, hosted on a logical datacenter, and a member of a Service Instance.")

P["cloud_network"] = prof("cloud_resource",
    rels=[R("cmdb_ci_network_service_instance", DEP, S, "up", "O", "Manual"),
          R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"),
          R(S, HOST, "cmdb_ci_logical_datacenter", "down", "M", "Cloud discovery / Service Graph Connector")],
    trace="Business Application -> Service Instance -> VM Instance / cloud resource -> (attached to) -> {L} -> " + CLOUD_TAIL,
    orphan="Network resource not hosted on a logical datacenter, or owned by no Dynamic CI Group / Network Service Instance.",
    audit="object_id populated; hosted on a logical datacenter; owned through the cloud networking offering.",
    csdm="Shared cloud network resource: usually serves many services, so ownership is through a Technology Management Offering (Dynamic CI Group) or a Network Service Instance.",
    cert="Cloud network owner; quarterly",
    gate="Pass if hosted on a logical datacenter and owned through the cloud networking offering.")

P["cloud_group"] = prof("cloud_resource",
    rels=[R(S, CONT, "cmdb_ci_cmp_resource", "up", "O", "Cloud discovery / Service Graph Connector"),
          R(S, HOST, "cmdb_ci_logical_datacenter", "down", "M", "Cloud discovery / Service Graph Connector")],
    trace="Business Application -> Service Instance -> cloud resource -> (grouped by) -> {L} -> " + CLOUD_TAIL,
    orphan="Grouping object with no resources and no logical datacenter.",
    audit="Hosted on / contained by a logical datacenter; naming standard followed; mandatory tags present.",
    csdm="Grouping construct: organises resources and often carries the tags that give them business context.",
    cert="Cloud platform owner; quarterly",
    gate="Pass if tied to a logical datacenter and tagged with application and owner.")

P["cloud_template"] = prof("cloud_resource",
    rec=["short_description"],
    rels=[R(S, HOST, "cmdb_ci_logical_datacenter", "down", "M", "Cloud discovery / Service Graph Connector")],
    up_text="No service relationship required: reference object (image, size, template, snapshot). Context is inherited from the instances provisioned from it.",
    trace="Business Application -> Service Instance -> VM Instance -> (provisioned from / snapshot of) -> {L} -> " + CLOUD_TAIL,
    orphan="Template or snapshot not hosted on a logical datacenter.",
    audit="Hosted on a logical datacenter; unused templates and aged snapshots reviewed.",
    csdm="Reference data for provisioning. Keep out of service maps; owned through the cloud platform offering.",
    cert="Cloud platform owner; yearly",
    gate="Pass if hosted on a logical datacenter. Not selectable on tasks.")

# ---------------------------------------------------------------- infrastructure: containers
P["k8s_cluster"] = prof("cloud_resource",
    req=["name", "operational_status", "discovery_source", "last_discovered"],
    key=["Verify in instance: cluster identifier fields"],
    ident="Verify in instance: identifier entries (cluster identifier / namespace-qualified name).",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Tag-based service mapping / manual"),
          R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"),
          R(S, HOST, "cmdb_ci_logical_datacenter", "down", "Mandatory (managed cloud Kubernetes)", "Cloud discovery / Kubernetes discovery")],
    trace=TOP + "Kubernetes workload -> Namespace -> Contains::Contained by (child of) -> {L} -> " + CLOUD_TAIL + " (on-premises: nodes -> Server)",
    source="Kubernetes discovery (Visibility agent / pattern) / cloud discovery",
    orphan="Cluster with no namespaces, or with no hosting datacenter / nodes.",
    stale="7 days without discovery update.",
    audit="Owner group populated; hosted on a logical datacenter or nodes resolve to servers; version in support.",
    csdm="Container platform: owned through a Technology Management Offering; workloads inside it link to Service Instances.",
    cert="Container platform owner; quarterly",
    gate="Pass if owner set, hosting resolved, and namespaces are discovered.", conf="Low")

P["k8s_obj"] = prof("k8s_cluster",
    rels=[R("cmdb_ci_service_auto", DEP, S, "up", "Mandatory (workloads: Service, Deployment, StatefulSet, DaemonSet)", "Tag-based service mapping (labels)"),
          R("cmdb_ci_kubernetes_namespace", CONT, S, "down", "M", "Kubernetes discovery")],
    host="Dependent on its Namespace / Cluster (containment). Verify the containment rule.",
    trace=TOP + "{L} -> Contains::Contained by (child of) -> Kubernetes Namespace -> Kubernetes Cluster -> " + CLOUD_TAIL,
    dep="Dependent",
    orphan="Object with no namespace / cluster, or workload with no Service Instance (missing labels).",
    stale="3 days without discovery update (short-lived objects).",
    dup="Objects are recreated frequently. Identify by cluster + namespace + name, not by transient identifiers, to avoid churn.",
    audit="Namespace and cluster resolved; application and owner labels present.",
    csdm="Kubernetes object: workloads link to a Service Instance by label; everything else inherits through namespace and cluster.",
    cert="Service Instance owner (from labels); quarterly",
    gate="Pass if namespace and cluster resolve and application / owner labels are present.")

P["container"] = prof("k8s_obj",
    rels=[R("cmdb_ci_kubernetes_pod", CONT, S, "up", "Mandatory (Kubernetes)", "Kubernetes discovery")],
    down_text="Verify in instance: relationship to the container engine / node that runs it.",
    trace=TOP + "Kubernetes workload -> Pod -> Contains::Contained by -> {L} -> node / container engine -> Server",
    orphan="Container with no pod or engine.",
    stale="1 to 3 days without discovery update. Consider not gating individual containers; govern the workload.",
    audit="Parent pod or engine resolved; image recorded.",
    csdm="Ephemeral runtime object: do not select on tasks; govern at workload and Service Instance level.",
    cert="Not certified individually",
    gate="Informational: accept if the parent pod / engine passes.")

# ---------------------------------------------------------------- infrastructure: facilities, end user, OT
P["facility"] = prof(
    req=["name", "location", "operational_status"], rec=["short_description", "company", "managed_by_group"],
    key=["location"],
    ident="Independent. Match on name within location (verify identifier entry).",
    rels=[R("cmdb_ci_facility_service_instance", DEP, S, "up", "O", "Manual")],
    down_text="Reference field: location (cmn_location, Foundation domain).",
    trace="Business Application -> Service Instance -> Application -> Server -> Located in::Houses -> Rack -> Computer Room -> Data Center -> location (Foundation)",
    source="Manual / DCIM import",
    orphan="Facility record with no location, or housing no CIs.",
    stale="180 days without update or attestation.",
    dup="Facilities data often exists in both DCIM and CMDB. DCIM is authoritative; import through IRE.",
    audit="Location populated; owner group populated; child spaces / racks present.",
    csdm="Physical end of every on-premises trace; links infrastructure to Foundation location data. Owned through a Facility Service Instance or facilities offering.",
    cert="Facilities / data center manager; every 6 months",
    gate="Pass if location and owner group are set and the parent space is linked.")

P["facility_eq"] = prof("facility",
    req=["name", "serial_number", "model_id", "location", "operational_status"], rec=["manufacturer", "asset", "short_description"],
    key=["serial_number", "model_id"],
    rels=[R("cmdb_ci_facility_service_instance", DEP, S, "up", "M", "Manual"),
          R(S, LOC, "cmdb_ci_computer_room", "down", "M", "Manual / DCIM import")],
    down_text="",
    trace="Business Application -> Service Instance -> Facility Service Instance -> Depends on::Used by -> {L} -> Located in::Houses -> Computer Room -> Data Center",
    orphan="Equipment with no room / location, or in no Facility Service Instance.",
    audit="Serial number and model populated; room and location populated; maintenance owner populated.",
    gate="Pass if identified by serial number, placed in a room, and part of a Facility Service Instance.")

P["enduser"] = prof(
    req=["name", "serial_number", "model_id", "manufacturer", "assigned_to", "location", "operational_status"],
    rec=["asset", "asset_tag", "os", "os_version", "company", "last_discovered"],
    own=["assigned_to", "managed_by_group", "support_group"], key=["serial_number", "model_id", "assigned_to"],
    ident=HW_IDENT,
    rels=[R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query")],
    down_text="None: leaf device. Physical placement through location and the linked asset record.",
    trace="Business context from assigned_to (user, department, cost centre) -> End-user Computing offering -> Contains::Contained by -> Dynamic CI Group -> svc_ci_assoc -> {L} -> location / asset",
    source="Endpoint management connector (Intune, SCCM, Jamf) / Agent Client Collector / asset receiving",
    orphan="Device with no assigned user or stockroom, or outside every end-user Dynamic CI Group.",
    stale="60 days without discovery update (devices can be off the network).",
    dup="Several endpoint tools report the same device. Serial number is the key; set one tool as authoritative per attribute.",
    audit="Serial number populated; asset linked; assigned_to is an active user or the asset is in stock; OS in support.",
    csdm="End-user device: no per-device service relationship; supported through an end-user computing Technology Management Offering.",
    cert="End-user computing lead; quarterly",
    gate="Pass if serial number, model, asset link and assigned user (or stockroom) are present.", conf="Medium")

P["ot"] = prof(
    req=["name", "serial_number", "model_id", "manufacturer", "location", "operational_status"],
    rec=["ip_address", "mac_address", "firmware_version", "Verify in instance: OT-specific fields (zone, level, protocol)"],
    key=["serial_number", "model_id", "Verify in instance: OT-specific identifiers"],
    ident="Verify in instance: OT classes use their own identifier entries in addition to the Hardware Rule.",
    rels=[R("cmdb_ci_operational_process_service_instance", DEP, S, "up", "M", "Manual / OT discovery")],
    down_text="Verify in instance: OT hierarchy placement (site / area / level) and network zone. location is mandatory.",
    trace="Business Application -> Service Instance -> Operational Process Service Instance -> Depends on::Used by -> {L} -> site / area (location)",
    source="OT discovery / OT security vendor integration",
    orphan="OT device in no Operational Process Service Instance, or with no location.",
    stale="60 days without discovery update (passive OT discovery).",
    dup="IT discovery and OT tools can both create the device. OT source is authoritative; exclude OT ranges from IT discovery.",
    audit="Location and owner group populated; firmware recorded; member of an Operational Process Service Instance.",
    csdm="OT / IoT device: tied to the production process it supports through an Operational Process Service Instance (new in CSDM 5).",
    cert="Plant / OT owner; every 6 months",
    gate="Pass if identified, located, and part of an Operational Process Service Instance.", conf="Low")

# ---------------------------------------------------------------- class inventory
# batch: (title, context, domain, default category, rows)
# row: table|label|parent|profile|flags|category     flags: v verify class, q parent unverified, P principal, a abstract, L low confidence
BATCHES = [
("Business context", "Business", "Design & Planning", "Business", """
cmdb_ci_business_app|Business Application|cmdb_ci|bizapp|P|Business application
cmdb_ci_business_capability|Business Capability|cmdb_ci|design|v|Business capability
cmdb_ci_business_process|Business Process|cmdb_ci|design||Business process
cmdb_ci_information_object|Information Object|cmdb_ci|design||Information object
cmdb_ci_service|Service|cmdb_ci|svc_base|a|Service (abstract parent)
cmdb_ci_service_business|Business Service|cmdb_ci_service|bizservice|P|Business service
service_offering|Service Offering|cmdb_ci_service|offering|vP|Service offering
cmdb_ci_sdlc_component|SDLC Component|cmdb_ci|design|v|SDLC component
cmdb_ci_appl_ai_application|AI & Model Application|cmdb_ci_appl|appl|q|AI application
cmdb_ci_function_ai|AI Function|cmdb_ci|app_logical|qL|AI function
cmdb_ci_environment|Environment|cmdb_ci|app_logical|qL|Logical grouping
"""),
("Application context", "Application", "Service Delivery", "Service Instance", """
cmdb_ci_service_auto|Service Instance|cmdb_ci_service|svc_instance|P|
cmdb_ci_service_discovered|Mapped Application Service|cmdb_ci_service_auto|svc_instance|P|
cmdb_ci_service_calculated|Calculated Application Service|cmdb_ci_service_auto|svc_instance|vP|
cmdb_ci_service_by_tags|Tag-Based Application Service|cmdb_ci_service_auto|svc_instance|vP|
cmdb_ci_query_based_service|Dynamic CI Group|cmdb_ci_service_auto|dcg|vP|Dynamic CI Group
cmdb_ci_service_technical|Technology Management Service|cmdb_ci_service|techservice|P|Technology management service
cmdb_ci_data_service_instance|Data Service Instance|cmdb_ci_service_auto|svc_instance|q|
cmdb_ci_network_service_instance|Network Service Instance|cmdb_ci_service_auto|svc_instance|q|
cmdb_ci_connection_service_instance|Connection Service Instance|cmdb_ci_service_auto|svc_instance|q|
cmdb_ci_operational_process_service_instance|Operational Process Service Instance|cmdb_ci_service_auto|svc_instance|q|
cmdb_ci_facility_service_instance|Facility Service Instance|cmdb_ci_service_auto|svc_instance|q|
cmdb_ci_infra_service|Infrastructure Service|cmdb_ci|app_logical|qL|Legacy service
cmdb_ci_ot_system_service|OT System Service|cmdb_ci_service_auto|app_logical|qL|OT service
cmdb_ci_api|API|cmdb_ci|app_logical|q|API
cmdb_ci_managed_api|Managed API|cmdb_ci_api|app_logical|q|API
cmdb_ci_api_component|API Component|cmdb_ci|app_logical|q|API
cmdb_ci_api_gateway|API Gateway|cmdb_ci_appl|appl|q|API
cmdb_ci_endpoint|Endpoint|cmdb_ci|app_logical|P|Service Mapping endpoint
cmdb_ci_batch_job|Batch Job|cmdb_ci|app_logical|q|Batch job
cmdb_ci_application_cluster|Application Cluster|cmdb_ci|app_logical|q|Application cluster
"""),
("Applications, middleware, web", "Infrastructure", "Service Delivery", "Application", """
cmdb_ci_appl|Application|cmdb_ci|appl|P|
cmdb_ci_appl_generic|Generic Application|cmdb_ci_appl|appl||
cmdb_ci_appl_now_app|ServiceNow Application|cmdb_ci_appl|appl||
cmdb_ci_appl_dot_net|.NET Application|cmdb_ci_appl|appl||
cmdb_ci_app_server|Application Server|cmdb_ci_appl|appl|P|Application server
cmdb_ci_app_server_java|JavaServer|cmdb_ci_app_server|appl||Application server
cmdb_ci_app_server_tomcat|Tomcat|cmdb_ci_app_server|appl||Application server
cmdb_ci_app_server_tomcat_war|Tomcat WAR|cmdb_ci_appl|component|q|Application component
cmdb_ci_app_server_jboss|JBoss|cmdb_ci_app_server|appl||Application server
cmdb_ci_app_server_weblogic|BEA Weblogic|cmdb_ci_app_server|appl||Application server
cmdb_ci_app_server_websphere|IBM Websphere|cmdb_ci_app_server|appl||Application server
cmdb_ci_websphere_cell|Websphere Cell|cmdb_ci|app_logical|q|Application cluster
cmdb_ci_appl_glassfish|GlassFish|cmdb_ci_appl|appl||Application server
cmdb_ci_web_server|Web Server|cmdb_ci_appl|appl|P|Web server
cmdb_ci_apache_web_server|Apache Web Server|cmdb_ci_web_server|appl||Web server
cmdb_ci_microsoft_iis_web_server|Microsoft IIS Web Server|cmdb_ci_web_server|appl||Web server
cmdb_ci_nginx_web_server|Nginx Web Server|cmdb_ci_web_server|appl||Web server
cmdb_ci_web_site|Web Site|cmdb_ci|component|q|Application component
cmdb_ci_web_application|Web Application|cmdb_ci|component|q|Application component
cmdb_ci_web_service|Web Service|cmdb_ci|component|q|Application component
cmdb_ci_appl_ibm_wmq|IBM MQ Manager|cmdb_ci_appl|appl||Messaging
cmdb_ci_appl_ibm_wmq_queue|IBM MQ Queue|cmdb_ci_appl|component|q|Messaging component
cmdb_ci_appl_ibm_wmb|IBM WebSphere Message Broker|cmdb_ci_appl|appl||Messaging
cmdb_ci_appl_rabbitmq|RabbitMQ|cmdb_ci_appl|appl||Messaging
cmdb_ci_appl_rabbitmq_cluster|RabbitMQ Cluster|cmdb_ci|app_logical|q|Application cluster
cmdb_ci_appl_msmq|MSMQ|cmdb_ci_appl|appl||Messaging
cmdb_ci_appl_tibco_message|Tibco Enterprise Message Service|cmdb_ci_appl|appl||Messaging
cmdb_ci_appl_biztalk|BizTalk|cmdb_ci_appl|appl||Integration
cmdb_ci_appl_sharepoint|SharePoint|cmdb_ci_appl|appl||Collaboration
cmdb_ci_appl_active_directory|Active Directory Service|cmdb_ci_appl|appl||Directory
cmdb_ci_ad_controller|Active Directory Domain Controller|cmdb_ci_appl|appl|q|Directory
cmdb_ci_ad_domain|AD Domain|cmdb_ci|app_logical|q|Directory (logical)
cmdb_ci_directory_ad_forest|AD Forest|cmdb_ci|app_logical|q|Directory (logical)
cmdb_ci_directory_server|Directory Server|cmdb_ci_appl|appl||Directory
cmdb_ci_directory_ldap|LDAP DB|cmdb_ci_directory_server|appl|q|Directory
cmdb_ci_email_server|Email Server|cmdb_ci_appl|appl||Email
cmdb_ci_exchange_mailbox_server|Exchange Mailbox Server|cmdb_ci_appl|appl|q|Email
cmdb_ci_exchange_cas|Exchange Client Access Server|cmdb_ci_appl|appl|q|Email
cmdb_ci_ftp_server|FTP Server|cmdb_ci_appl|appl||File transfer
cmdb_ci_appl_citrix_xenapp|Citrix XenApp or Presentation Server|cmdb_ci_appl|appl||Application delivery
cmdb_ci_appl_controlm|Control-M|cmdb_ci_appl|appl||Scheduling
cmdb_ci_appl_peoplesoft|Peoplesoft Application Server|cmdb_ci_appl|appl||ERP
cmdb_ci_appl_sap_ci|SAP CI Application|cmdb_ci_appl|appl||ERP (SAP)
cmdb_ci_appl_sap_di|SAP DI Application|cmdb_ci_appl|appl||ERP (SAP)
cmdb_ci_appl_sap_ascs|SAP ASCS Application|cmdb_ci_appl|appl||ERP (SAP)
cmdb_ci_appl_sap_scs|SAP SCS Application|cmdb_ci_appl|appl||ERP (SAP)
cmdb_ci_appl_sap_bus_obj|SAP Business Objects|cmdb_ci_appl|appl||ERP (SAP)
cmdb_ci_appl_sap_hana_db|SAP Hana Db|cmdb_ci_appl|appl||ERP (SAP)
cmdb_ci_appl_ora_ebs|Oracle ESB|cmdb_ci_appl|appl||ERP (Oracle)
cmdb_ci_appl_ora_http|Oracle HTTP Server|cmdb_ci_appl|appl||Web server
cmdb_ci_appl_ora_tnslsnr|Oracle TNS Listener Engine|cmdb_ci_appl|appl||Database listener
cmdb_ci_config_automation_server|Management Server|cmdb_ci_appl|appl|q|Configuration automation
cmdb_ci_windows_service|Windows Service|cmdb_ci|component|q|OS component
cmdb_ci_unix_daemon|UNIX Daemon|cmdb_ci|component|q|OS component
cmdb_ci_config_file|Configuration File|cmdb_ci|component|q|Application component
cmdb_ci_spkg|Software|cmdb_ci|component||Software package
cmdb_ci_certificate|Unique Certificate|cmdb_ci|certificate||Certificate
cmdb_ci_base_rpa_robot|Base Robot|cmdb_ci|app_logical|qL|RPA
cmdb_ci_base_rpa_process|Base Bot Process|cmdb_ci|app_logical|qL|RPA
"""),
("Databases", "Infrastructure", "Service Delivery", "Database", """
cmdb_ci_database|Database|cmdb_ci|db_catalog||Database catalog
cmdb_ci_db_instance|Database Instance|cmdb_ci_appl|db_instance|P|Database instance
cmdb_ci_db_catalog|Database Catalog|cmdb_ci_database|db_catalog|q|Database catalog
cmdb_ci_db_mssql_instance|MSFT SQL Instance|cmdb_ci_db_instance|db_instance|P|Database instance
cmdb_ci_db_mssql_catalog|MSFT SQL Catalog|cmdb_ci_db_catalog|db_catalog||Database catalog
cmdb_ci_db_mssql_analysis|SQL Server Analysis Services|cmdb_ci_appl|appl|q|Database service
cmdb_ci_db_mssql_integration|SQL Server Integration Services|cmdb_ci_appl|appl|q|Database service
cmdb_ci_db_mssql_reporting|SQL Server Reporting Services|cmdb_ci_appl|appl|q|Database service
cmdb_ci_db_ora_instance|Oracle Instance|cmdb_ci_db_instance|db_instance|P|Database instance
cmdb_ci_db_ora_catalog|Oracle Catalog|cmdb_ci_db_catalog|db_catalog||Database catalog
cmdb_ci_db_ora_listener|Oracle Database Listener|cmdb_ci_appl|appl|q|Database listener
cmdb_ci_db_mysql_instance|MySQL Instance|cmdb_ci_db_instance|db_instance||Database instance
cmdb_ci_db_mysql_catalog|MySQL Catalog|cmdb_ci_db_catalog|db_catalog||Database catalog
cmdb_ci_db_postgresql_instance|PostgreSQL Instance|cmdb_ci_db_instance|db_instance||Database instance
cmdb_ci_db_db2_instance|DB2 Instance|cmdb_ci_db_instance|db_instance||Database instance
cmdb_ci_db_db2_catalog|DB2 Catalog|cmdb_ci_db_catalog|db_catalog||Database catalog
cmdb_ci_db_mongodb_instance|MongoDB Instance|cmdb_ci_db_instance|db_instance||Database instance
cmdb_ci_db_syb_instance|Sybase Instance|cmdb_ci_db_instance|db_instance||Database instance
cmdb_ci_db_hbase_instance|HBase Instance|cmdb_ci_db_instance|db_instance||Database instance
"""),
("Compute hardware and clusters", "Infrastructure", "Service Delivery", "Compute", """
cmdb_ci_hardware|Hardware|cmdb_ci|server|a|Hardware (abstract parent)
cmdb_ci_computer|Computer|cmdb_ci_hardware|server|a|Compute (abstract parent)
cmdb_ci_server|Server|cmdb_ci_computer|server|P|
cmdb_ci_win_server|Windows Server|cmdb_ci_server|server|P|
cmdb_ci_linux_server|Linux Server|cmdb_ci_server|server|P|
cmdb_ci_unix_server|UNIX Server|cmdb_ci_server|server|P|
cmdb_ci_aix_server|AIX Server|cmdb_ci_unix_server|server||
cmdb_ci_solaris_server|Solaris Server|cmdb_ci_unix_server|server||
cmdb_ci_hpux_server|HPUX Server|cmdb_ci_unix_server|server||
cmdb_ci_osx_server|OS/X Server|cmdb_ci_server|server||
cmdb_ci_netware_server|Netware Server|cmdb_ci_server|server||
cmdb_ci_esx_server|ESX Server|cmdb_ci_virtualization_server|hypervisor|qP|Hypervisor host
cmdb_ci_hyper_v_server|Hyper-V Server|cmdb_ci_virtualization_server|hypervisor|q|Hypervisor host
cmdb_ci_virtualization_server|Virtualization Server|cmdb_ci_server|hypervisor|q|Hypervisor host
cmdb_ci_mainframe|IBM Mainframe|cmdb_ci_server|server|q|Mainframe
cmdb_ci_mainframe_lpar|IBM Mainframe LPAR|cmdb_ci_server|server|q|Mainframe
cmdb_ci_mainframe_hardware|Mainframe Hardware|cmdb_ci_hardware|chassis|q|Mainframe
cmdb_ci_ibm_i_server|IBM i Server|cmdb_ci_server|server|q|Midrange
cmdb_ci_hmc_server|IBM HMC Server|cmdb_ci_server|server|q|Midrange
cmdb_ci_lpar_instance|IBM LPAR Instance|cmdb_ci_vm_instance|vm|q|Virtual machine
cmdb_ci_chassis_server|Server Chassis|cmdb_ci_hardware|chassis|q|Enclosure
cmdb_ci_ucs_chassis|Cisco UCS Chassis|cmdb_ci_ucs_equipment|chassis|q|Enclosure
cmdb_ci_ucs_blade|Cisco UCS Blade|cmdb_ci_ucs_equipment|chassis|q|Enclosure
cmdb_ci_converged_infra|Converged Infrastructure|cmdb_ci_hardware|chassis|qL|Converged infrastructure
cmdb_ci_datapower_server|Data Power Hosting Server|cmdb_ci_server|server|q|Appliance
cmdb_ci_net_app_server|Network Appliance Hardware|cmdb_ci_server|server|q|Appliance
cmdb_ci_tape_server|Server Tape Unit|cmdb_ci_server|server|q|Appliance
cmdb_ci_win_domain_controller|Windows Domain Controller|cmdb_ci_win_server|server|q|
cmdb_ci_cluster|Cluster|cmdb_ci|cluster|P|Cluster
cmdb_ci_cluster_node|Cluster Node|cmdb_ci|component||Cluster component
cmdb_ci_cluster_resource|Cluster Resource|cmdb_ci|component||Cluster component
cmdb_ci_cluster_vip|Cluster Virtual IP|cmdb_ci|component||Cluster component
cmdb_ci_win_cluster|Windows Cluster|cmdb_ci_cluster|cluster||Cluster
cmdb_ci_win_cluster_node|Windows Cluster Node|cmdb_ci_cluster_node|component||Cluster component
cmdb_ci_unix_cluster|UNIX Cluster|cmdb_ci_cluster|cluster||Cluster
cmdb_ci_host_cluster|Host Cluster|cmdb_ci|cluster|q|Cluster
cmdb_ci_gpu|Graphics Processing Unit|cmdb_ci|component|q|Hardware component
cmdb_ci_memory_module|Memory Module|cmdb_ci|component|q|Hardware component
cmdb_ci_unclassified_hardware|Unclassed Hardware|cmdb_ci_hardware|server|a|Holding class
cmdb_ci_incomplete_ip|Incomplete IP Identified Device|cmdb_ci_hardware|server|qa|Holding class
"""),
("Network", "Infrastructure", "Service Delivery", "Network device", """
cmdb_ci_netgear|Network Gear|cmdb_ci_hardware|netgear|P|
cmdb_ci_ip_router|IP Router|cmdb_ci_netgear|netgear|P|
cmdb_ci_ip_switch|IP Switch|cmdb_ci_netgear|netgear|P|
cmdb_ci_ip_firewall|IP Firewall|cmdb_ci_netgear|netgear|P|
cmdb_ci_ip_device|IP Device|cmdb_ci_hardware|netgear|q|
cmdb_ci_wap_network|Wireless Access Point|cmdb_ci_netgear|netgear|q|
cmdb_ci_network_controller|Network Controller|cmdb_ci_netgear|netgear|q|
cmdb_ci_sdwan_controller|SDWAN Controller|cmdb_ci_netgear|netgear|q|
cmdb_ci_sdwan_edge|SDWAN Edge|cmdb_ci_netgear|netgear|q|
cmdb_ci_nids|Network Intrusion Detection System|cmdb_ci_netgear|netgear|q|
cmdb_ci_outofband_device|Out-of-Band Device|cmdb_ci_hardware|netgear|q|
cmdb_ci_lb|Load Balancer|cmdb_ci_netgear|netgear|qP|Load balancer
cmdb_ci_lb_bigip|F5 BIG-IP|cmdb_ci_lb|netgear||Load balancer
cmdb_ci_lb_f5_ltm|F5 BigIP LTM|cmdb_ci_lb|netgear|q|Load balancer
cmdb_ci_lb_f5_gtm|F5 BigIP GTM|cmdb_ci_lb|netgear|q|Load balancer
cmdb_ci_lb_netscaler|Citrix Netscaler|cmdb_ci_lb|netgear||Load balancer
cmdb_ci_lb_a10|A10 Load Balancer|cmdb_ci_lb|netgear||Load balancer
cmdb_ci_lb_haproxy|HAProxy Load Balancer|cmdb_ci_lb_appl|appl|q|Load balancer (software)
cmdb_ci_lb_nginx|Nginx Load Balancer|cmdb_ci_lb_appl|appl|q|Load balancer (software)
cmdb_ci_lb_appl|Load Balancer Application|cmdb_ci_appl|appl||Load balancer (software)
cmdb_ci_lb_service|Load Balancer Service|cmdb_ci|lb_logical||Load balancer (logical)
cmdb_ci_lb_pool|Load Balancer Pool|cmdb_ci|lb_logical||Load balancer (logical)
cmdb_ci_lb_pool_member|Load Balancer Pool Member|cmdb_ci|component||Load balancer component
cmdb_ci_ip_network|IP Network|cmdb_ci|net_logical||Network (logical)
cmdb_ci_ip_address|IP Address|cmdb_ci|component||Network component
cmdb_ci_network_adapter|Network Adapter|cmdb_ci|component||Network component
cmdb_ci_port|Port|cmdb_ci|component|q|Network component
cmdb_ci_dns_name|DNS Name|cmdb_ci|net_logical||DNS
cmdb_ci_vpn|Virtual Private Network|cmdb_ci|net_logical||Network (logical)
cmdb_ci_circuit|Circuit|cmdb_ci|net_logical||Circuit
cmdb_ci_network_circuit|Network Circuit|cmdb_ci|net_logical|q|Circuit
cmdb_ci_network_link|Network Link|cmdb_ci|net_logical|q|Circuit
cmdb_ci_ip_phone|IP Phone|cmdb_ci_comm|enduser|q|Voice
cmdb_ci_voice_gateway|Voice Gateway|cmdb_ci_netgear|netgear|q|Voice
cmdb_ci_fortinet_vdom|Fortinet Virtual Domain|cmdb_ci|net_logical|q|Firewall (logical)
"""),
("Storage", "Infrastructure", "Service Delivery", "Storage", """
cmdb_ci_storage_device|Storage Device|cmdb_ci|storage_hw|qP|Storage system
cmdb_ci_msd|Mass Storage Device|cmdb_ci_storage_device|storage_hw|q|Storage system
cmdb_ci_storage_server|Storage Server|cmdb_ci_server|server|v|Storage system
cmdb_ci_storage_controller|Storage Controller|cmdb_ci|component|q|Storage component
cmdb_ci_storage_switch|Storage Switch|cmdb_ci_netgear|netgear|q|Storage network
cmdb_ci_storage_pool|Storage Pool|cmdb_ci|component|q|Storage component
cmdb_ci_storage_volume|Storage Volume|cmdb_ci|component|q|Storage component
cmdb_ci_storage_fileshare|Storage File Share|cmdb_ci|component|q|Storage component
cmdb_ci_storage_hba|Storage HBA|cmdb_ci|component|q|Storage component
cmdb_ci_san|Storage Area Network|cmdb_ci|net_logical|q|Storage network
cmdb_ci_san_fabric|SAN Fabric|cmdb_ci|component|q|Storage network
cmdb_ci_san_zone|SAN Zone|cmdb_ci|component|q|Storage network
cmdb_ci_disk|Disk|cmdb_ci_storage_device|component|q|Storage component
cmdb_ci_file_system|File System|cmdb_ci_storage_volume|component|q|Storage component
cmdb_ci_nas_file_system|NAS File System|cmdb_ci_file_system|component|q|Storage component
cmdb_ci_datastore|Datastore|cmdb_ci|component|q|Storage component
cmdb_ci_netapp_cdot|NetApp CDOT|cmdb_ci_storage_device|storage_hw|q|Storage system
cmdb_ci_netapp_svm|NetApp SVM|cmdb_ci|component|q|Storage component
cmdb_ci_netapp_volume|NetApp Volume|cmdb_ci|component|q|Storage component
"""),
("Virtualisation", "Infrastructure", "Service Delivery", "Virtual machine", """
cmdb_ci_vm_object|Virtual Machine Object|cmdb_ci|vm|a|Virtualisation (abstract parent)
cmdb_ci_vm_instance|Virtual Machine Instance|cmdb_ci_vm_object|vm|P|
cmdb_ci_vm_template|Virtual Machine Template|cmdb_ci_vm_object|cloud_template|q|Template
cmdb_ci_vcenter|VMware vCenter Instance|cmdb_ci_appl|appl|P|Virtualisation manager
cmdb_ci_vcenter_datacenter|VMware vCenter Datacenter|cmdb_ci_vcenter_object|virt_obj|q|Virtualisation platform
cmdb_ci_vcenter_cluster|VMware vCenter Cluster|cmdb_ci_vcenter_object|virt_obj|q|Virtualisation platform
cmdb_ci_vcenter_datastore|VMware vCenter Datastore|cmdb_ci_vcenter_object|virt_obj|q|Virtualisation platform
cmdb_ci_vcenter_network|VMware vCenter Network|cmdb_ci_vcenter_object|virt_obj|q|Virtualisation platform
cmdb_ci_vcenter_folder|VMware vCenter Folder|cmdb_ci_vcenter_object|virt_obj|q|Virtualisation platform
cmdb_ci_esx_resource_pool|ESX Resource Pool|cmdb_ci_vcenter_object|virt_obj|q|Virtualisation platform
cmdb_ci_vmware_instance|VMware Virtual Machine Instance|cmdb_ci_vm_instance|vm|P|
cmdb_ci_vmware_template|VMware Virtual Machine Template|cmdb_ci_vm_template|cloud_template|q|Template
cmdb_ci_hyper_v_instance|Hyper-V Virtual Machine Instance|cmdb_ci_vm_instance|vm||
cmdb_ci_hyper_v_cluster|Hyper-V Cluster|cmdb_ci_hyper_v_object|virt_obj|q|Virtualisation platform
cmdb_ci_hyper_v_network|Hyper-V Virtual Network|cmdb_ci_hyper_v_object|virt_obj|q|Virtualisation platform
cmdb_ci_kvm|KVM|cmdb_ci|virt_obj|qL|Virtualisation platform
cmdb_ci_kvm_vm_instance|KVM Virtual Machine Instance|cmdb_ci_vm_instance|vm||
cmdb_ci_solaris_instance|Solaris Virtual Machine Instance|cmdb_ci_vm_instance|vm||
cmdb_ci_nutanix_cluster|Nutanix Cluster|cmdb_ci|virt_obj|q|Virtualisation platform
cmdb_ci_nutanix_host|Nutanix Host|cmdb_ci_server|hypervisor|q|Hypervisor host
cmdb_ci_nutanix_vm_instance|Nutanix Virtual Machine Instance|cmdb_ci_vm_instance|vm|q|
cmdb_ci_virtual_desktop|Virtual Desktop|cmdb_ci|enduser|qL|Virtual desktop
"""),
("Public and private cloud", "Infrastructure", "Service Delivery", "Cloud resource", """
cmdb_ci_cloud_service_account|Cloud Service Account|cmdb_ci|cloud_account|vP|Cloud account
cmdb_ci_logical_datacenter|Logical Datacenter|cmdb_ci|cloud_dc|P|Cloud datacenter
cmdb_ci_aws_datacenter|AWS Datacenter|cmdb_ci_logical_datacenter|cloud_dc|P|Cloud datacenter
cmdb_ci_azure_datacenter|Azure Datacenter|cmdb_ci_logical_datacenter|cloud_dc|P|Cloud datacenter
cmdb_ci_gcp_datacenter|Google Datacenter|cmdb_ci_logical_datacenter|cloud_dc|v|Cloud datacenter
cmdb_ci_openstack_datacenter|OpenStack Datacenter|cmdb_ci_logical_datacenter|cloud_dc||Cloud datacenter
cmdb_ci_netapp_datacenter|NetApp Datacenter|cmdb_ci_logical_datacenter|cloud_dc|q|Cloud datacenter
cmdb_ci_availability_zone|Availability Zone|cmdb_ci|cloud_group|v|Cloud grouping
cmdb_ci_availability_set|Availability Set|cmdb_ci|cloud_group|q|Cloud grouping
cmdb_ci_resource_group|Resource Group|cmdb_ci|cloud_group|q|Cloud grouping
cmdb_ci_cmp_resource|Cloud Resource|cmdb_ci|cloud_resource|qa|Cloud resource (generic)
cmdb_ci_ec2_instance|EC2 Virtual Machine Instance|cmdb_ci_vm_instance|vm||Cloud compute
cmdb_ci_os_template|Image|cmdb_ci|cloud_template|q|Cloud template
cmdb_ci_compute_template|Hardware Type|cmdb_ci|cloud_template|v|Cloud template
cmdb_ci_server_snapshot|Server Snapshot|cmdb_ci|cloud_template|q|Cloud snapshot
cmdb_ci_storage_vol_snapshot|Storage Volume Snapshot|cmdb_ci|cloud_template|q|Cloud snapshot
cmdb_ci_volume_template|Volume Template|cmdb_ci|cloud_template|q|Cloud template
cmdb_ci_cloud_object_storage|Cloud Object Storage|cmdb_ci|cloud_resource|v|Cloud storage
cmdb_ci_cloud_storage_account|Cloud Storage Account|cmdb_ci|cloud_resource|v|Cloud storage
cmdb_ci_cloud_database|Cloud Database|cmdb_ci|cloud_resource|qP|Cloud database
cmdb_ci_cloud_db_cluster|Cloud Database Cluster|cmdb_ci|cloud_resource|v|Cloud database
cmdb_ci_dynamodb_table|DynamoDB Table|cmdb_ci|cloud_resource|v|Cloud database
cmdb_ci_network|Cloud Network|cmdb_ci|cloud_network|q|Cloud network
cmdb_ci_subnet|Cloud Mgmt Subnet|cmdb_ci|cloud_network|q|Cloud network
cmdb_ci_cloud_subnet|Cloud Subnet|cmdb_ci|cloud_network|v|Cloud network
cmdb_ci_vpc|Virtual Private Cloud|cmdb_ci|cloud_network|q|Cloud network
cmdb_ci_nic|Cloud Mgmt Network Interface|cmdb_ci|component|q|Cloud network component
cmdb_ci_cloud_ip_address|Cloud IP Address|cmdb_ci|component|q|Cloud network component
cmdb_ci_cloud_public_ipaddress|Cloud Public IP Address|cmdb_ci|cloud_network|v|Cloud network
cmdb_ci_compute_security_group|Compute Security Group|cmdb_ci|cloud_network|v|Cloud network security
cmdb_ci_network_acl|Network ACL|cmdb_ci|cloud_network|q|Cloud network security
cmdb_ci_network_acl_rule|Network ACL Rule|cmdb_ci|component|q|Cloud network component
cmdb_ci_nat_gateway|NAT Gateway|cmdb_ci|cloud_network|q|Cloud network
cmdb_ci_virtual_pvt_gateway|Virtual Private Gateway|cmdb_ci|cloud_network|q|Cloud network
cmdb_ci_vpn_connection|VPN Connection|cmdb_ci|cloud_network|q|Cloud network
cmdb_ci_cloud_gateway|Cloud Gateway|cmdb_ci|cloud_network|v|Cloud network
cmdb_ci_cloud_load_balancer|Cloud Load Balancer|cmdb_ci|cloud_resource|v|Cloud load balancer
cmdb_ci_cloud_function|Cloud Function|cmdb_ci|cloud_resource|v|Cloud serverless
cmdb_ci_cloud_messaging_service|Cloud Messaging Service|cmdb_ci|cloud_resource|v|Cloud messaging
cmdb_ci_cloud_webserver|Cloud WebServer|cmdb_ci|cloud_resource|v|Cloud PaaS
cmdb_ci_cloud_appserver|Cloud Application Server|cmdb_ci|cloud_resource|v|Cloud PaaS
cmdb_ci_cloud_key_pair|Cloud Key Pair|cmdb_ci|cloud_template|vL|Cloud security object
cmdb_ci_cloud_ecs_cluster|AWS Cloud ECS Cluster|cmdb_ci|cloud_resource|v|Cloud containers
cmdb_ci_aws_api_gateway|AWS API Gateway|cmdb_ci|cloud_resource|q|Cloud API
cmdb_ci_azure_api_mgmt|Azure API Management|cmdb_ci|cloud_resource|q|Cloud API
cmdb_ci_web_acl|Web ACL|cmdb_ci|cloud_network|q|Cloud network security
cmdb_ci_sa_scaling_pol_base|Scaling Policy|cmdb_ci|cloud_template|q|Cloud configuration object
cmdb_ci_deployed_marketplace_product|Deployed Marketplace Product|cmdb_ci|cloud_resource|q|Cloud marketplace
cmdb_ci_dns_domain_info|DNS Domain Info|cmdb_ci|net_logical|q|DNS
cmdb_ci_dns_resource_record|DNS Resource Records|cmdb_ci|net_logical|q|DNS
"""),
("Containers and platforms", "Infrastructure", "Service Delivery", "Kubernetes", """
cmdb_ci_kubernetes_cluster|Kubernetes Cluster|cmdb_ci|k8s_cluster|vP|
cmdb_ci_kubernetes_node|Kubernetes Node|cmdb_ci|k8s_obj|v|
cmdb_ci_kubernetes_node_pool|Kubernetes Node Pool|cmdb_ci|k8s_obj|q|
cmdb_ci_kubernetes_namespace|Kubernetes Namespace|cmdb_ci|k8s_obj|v|
cmdb_ci_kubernetes_pod|Kubernetes Pod|cmdb_ci_kubernetes_component|k8s_obj|v|
cmdb_ci_kubernetes_service|Kubernetes Service|cmdb_ci_kubernetes_component|k8s_obj|v|Kubernetes workload
cmdb_ci_kubernetes_deployment|Kubernetes Deployment|cmdb_ci_kubernetes_component|k8s_obj|v|Kubernetes workload
cmdb_ci_kubernetes_statefulset|Kubernetes StatefulSet|cmdb_ci_kubernetes_component|k8s_obj|v|Kubernetes workload
cmdb_ci_kubernetes_daemonset|Kubernetes DaemonSet|cmdb_ci_kubernetes_component|k8s_obj|v|Kubernetes workload
cmdb_ci_kubernetes_replicaset|Kubernetes ReplicaSet|cmdb_ci_kubernetes_component|k8s_obj|v|Kubernetes workload
cmdb_ci_kubernetes_component|Kubernetes Component|cmdb_ci|k8s_obj|qa|Kubernetes (abstract parent)
cmdb_ci_docker|Docker Container|cmdb_ci_oslv_container|container|q|Container
cmdb_ci_docker_engine|Docker Engine|cmdb_ci_oslv_engine|appl|q|Container engine
cmdb_ci_docker_image|Docker Image|cmdb_ci_oslv_image|container|q|Container image
cmdb_ci_oslv_container|OS-level Virtualization Container|cmdb_ci|container|q|Container
cmdb_ci_oslv_engine|OS-level Virtualization Engine|cmdb_ci_appl|appl|q|Container engine
cmdb_ci_oslv_image|OS-level Virtualization Image|cmdb_ci|container|q|Container image
cmdb_ci_pcf_component|CloudFoundry Component|cmdb_ci|app_logical|qL|PaaS component
cmdb_ci_deployment_component|Deployment Component|cmdb_ci|app_logical|qL|PaaS component
"""),
("Facilities, end-user devices, OT and IoT", "Infrastructure", "Service Delivery", "Facility", """
cmdb_ci_datacenter|Data Center|cmdb_ci|facility|P|
cmdb_ci_zone|Data Center Zone|cmdb_ci|facility|q|
cmdb_ci_computer_room|Computer Room|cmdb_ci|facility|q|
cmdb_ci_rack|Rack|cmdb_ci|facility|P|
cmdb_ci_pdu|PDU|cmdb_ci|facility_eq|q|Facility equipment
cmdb_ci_ups|UPS|cmdb_ci|facility_eq|q|Facility equipment
cmdb_ci_crac|Computer Room AC|cmdb_ci|facility_eq|q|Facility equipment
cmdb_ci_hvac|HVAC Equipment|cmdb_ci_facility_hardware|facility_eq|q|Facility equipment
cmdb_ci_generator_power_eq|Power Generator|cmdb_ci_power_eq|facility_eq|q|Facility equipment
cmdb_ci_facility_hardware|Facility Hardware|cmdb_ci_hardware|facility_eq|q|Facility equipment
cmdb_ci_pc_hardware|Personal Computer|cmdb_ci_computer|enduser|P|End-user device
cmdb_ci_handheld_computing|Handheld Computing Device|cmdb_ci_computer|enduser|q|End-user device
cmdb_ci_printer|Printer|cmdb_ci_hardware|enduser|q|Printer
cmdb_ci_mfp_printer|Multi-function Printer|cmdb_ci_printer|enduser||Printer
cmdb_ci_peripheral|Computer Peripheral|cmdb_ci_hardware|enduser|q|Peripheral
cmdb_ci_display|Display Device|cmdb_ci_hardware|enduser|q|Peripheral
cmdb_ci_comm|Communication Device|cmdb_ci_hardware|enduser|q|Communication device
cmdb_ci_iot|IoT Device|cmdb_ci_hardware|ot|q|IoT
cmdb_ci_edge_device|Edge Device|cmdb_ci_hardware|ot|q|IoT / edge
cmdb_ci_security|Security Device|cmdb_ci_hardware|ot|q|Physical security
cmdb_ci_ot|Operational Technology (OT)|cmdb_ci_hardware|ot|qP|OT
cmdb_ci_ot_plc|PLC|cmdb_ci_ot_control|ot|q|OT
cmdb_ci_ot_hmi|HMI|cmdb_ci_ot_supervisory|ot|q|OT
cmdb_ci_ot_scada_server|SCADA Server|cmdb_ci_ot_supervisory|ot|q|OT
cmdb_ci_ot_historian|Historian|cmdb_ci_ot_supervisory|ot|q|OT
cmdb_ci_ot_control|OT Control System|cmdb_ci_ot|ot|q|OT
cmdb_ci_ot_field_device|OT Field Device|cmdb_ci_ot|ot|q|OT
cmdb_ci_med_device|Medical Device|cmdb_ci_hardware|ot|q|Medical device
"""),
]

CLASS_MODELS = set("""cmdb_ci_api cmdb_ci_api_component cmdb_ci_api_gateway cmdb_ci_managed_api cmdb_ci_appl_ai_application cmdb_ci_function_ai
cmdb_ci_aws_api_gateway cmdb_ci_azure_api_mgmt cmdb_ci_certificate cmdb_ci_connection_service_instance cmdb_ci_data_service_instance
cmdb_ci_network_service_instance cmdb_ci_operational_process_service_instance cmdb_ci_facility_service_instance cmdb_ci_converged_infra
cmdb_ci_deployed_marketplace_product cmdb_ci_deployment_component cmdb_ci_display cmdb_ci_dns_domain_info cmdb_ci_dns_resource_record
cmdb_ci_edge_device cmdb_ci_fortinet_vdom cmdb_ci_gpu cmdb_ci_handheld_computing cmdb_ci_hmc_server cmdb_ci_ibm_i_server cmdb_ci_incomplete_ip
cmdb_ci_iot cmdb_ci_kubernetes_node_pool cmdb_ci_lpar_instance cmdb_ci_med_device cmdb_ci_network_circuit cmdb_ci_network_controller
cmdb_ci_network_link cmdb_ci_nids cmdb_ci_nutanix_cluster cmdb_ci_nutanix_host cmdb_ci_nutanix_vm_instance cmdb_ci_ot cmdb_ci_ot_plc cmdb_ci_ot_hmi
cmdb_ci_ot_scada_server cmdb_ci_ot_historian cmdb_ci_ot_control cmdb_ci_ot_field_device cmdb_ci_ot_system_service cmdb_ci_sdwan_controller
cmdb_ci_sdwan_edge cmdb_ci_security cmdb_ci_unclassified_hardware cmdb_ci_voice_gateway cmdb_ci_web_acl""".split())

EXTRA_LABELS = {"cmdb_ci": "Configuration Item"}

VERIFY_REL = "Verify in instance (containment relationship or reference field)"

# ---------------------------------------------------------------- per-class overrides
def via(parent, rel=VERIFY_REL, by="Discovery"):
    return dict(via=parent, rels=[R(parent, rel, S, "up", "M", by)])

OV = {
 # business
 "cmdb_ci_business_capability": dict(rels=[R("cmdb_ci_business_app", PROV, S, "down", "M", "Manual / APM")],
    up_text="None: top of the business context (capability hierarchy through the parent capability).",
    trace="{L} -> Provides::Provided by (provided by) -> Business Application -> Consumes::Consumed by -> Service Instance -> infrastructure CIs",
    orphan="Leaf capability that no Business Application provides."),
 "cmdb_ci_business_process": dict(down_text="Verify in instance: link to Business Application (APM business process reference)."),
 "cmdb_ci_information_object": dict(down_text="Verify in instance: link to the Business Applications and Data Service Instances that hold or use the information.",
    audit="Owner populated; data classification recorded (verify field); linked to at least one Business Application."),
 "cmdb_ci_sdlc_component": dict(domain="Build & Integration", down_text="Verify in instance: link from SDLC Component to its Business Application.",
    csdm="Build & Integration record: represents the code component / repository behind a Business Application."),
 "cmdb_ci_service": dict(domain="Service Consumption"),
 "cmdb_ci_service_business": dict(domain="Service Consumption"),
 "service_offering": dict(domain="Service Consumption"),
 "cmdb_ci_appl_ai_application": dict(ctx="Infrastructure", domain="Service Delivery",
    note="Listed in the business batch of the inventory; modelled as an infrastructure application CI because it extends Application. Verify the AI-specific fields added by CMDB CI Class Models."),
 "cmdb_ci_function_ai": dict(ctx="Application", domain="Build & Integration",
    note="New AI class. Parent class, fields and relationships must be confirmed in the instance."),
 "cmdb_ci_environment": dict(ctx="Application", domain="Service Delivery",
    note="Logical grouping class from cloud management. Do not confuse with the environment attribute on CIs."),
 # application context
 "cmdb_ci_service_auto": dict(note="Use this class only for manually built services; prefer Mapped, Calculated or Tag-Based where a population method exists."),
 "cmdb_ci_service_discovered": dict(source="Service Mapping (top-down, entry point based)",
    rels=[R("cmdb_ci_business_app", CONS, S, "up", "M", "Manual / APM"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_endpoint", "down", "M", "Service Mapping (entry point)"), R(S, ASSOC, "cmdb_ci", "down", "M", "Service Mapping")],
    stale="60 days without a successful Service Mapping recomputation."),
 "cmdb_ci_service_calculated": dict(source="Calculated population (CMDB query, Dynamic CI Group, relationship levels) / connector",
    req_add=["populator_status", "service_populator"],
    rels=[R("cmdb_ci_business_app", CONS, S, "up", "M", "Manual / APM"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_appl", "down", "M", "Manual relationships + calculated population"), R(S, ASSOC, "cmdb_ci", "down", "M", "Calculated population")]),
 "cmdb_ci_service_by_tags": dict(source="Tag-based service mapping (cloud / Kubernetes tags)",
    key_add=["Verify in instance: tag family and tag value fields"],
    rels=[R("cmdb_ci_business_app", CONS, S, "up", "M", "Manual / APM"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, ASSOC, "cmdb_ci", "down", "M", "Tag-based service mapping")],
    trace=TOP.replace("Service Instance -> Depends on::Used by -> ", "{L} -> svc_ci_assoc -> ") + "tagged cloud resource -> " + CLOUD_TAIL),
 "cmdb_ci_data_service_instance": dict(rels=[R("cmdb_ci_business_app", CONS, S, "up", "M", "Manual / APM"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_db_instance", "down", "M", "Manual"), R(S, DEP, "cmdb_ci_cloud_database", "down", "O", "Manual")],
    trace=TOP.replace("Service Instance", "{L}") + "Database Instance / Cloud Database -> Runs on::Runs -> Server (or " + CLOUD_TAIL + ")"),
 "cmdb_ci_network_service_instance": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Manual"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_netgear", "down", "M", "Manual")],
    trace="Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> {L} -> Depends on::Used by -> Network Gear -> Located in::Houses -> Rack -> Data Center"),
 "cmdb_ci_connection_service_instance": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Manual"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_circuit", "down", "M", "Manual")],
    trace="Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> {L} -> Depends on::Used by -> Circuit / Network Link -> provider"),
 "cmdb_ci_operational_process_service_instance": dict(rels=[R("cmdb_ci_business_app", CONS, S, "up", "M", "Manual / APM"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_ot", "down", "M", "Manual / OT discovery")],
    trace=TOP.replace("Service Instance", "{L}") + "Operational Technology (OT) devices -> site / area (location)"),
 "cmdb_ci_facility_service_instance": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Manual"), R("service_offering", DEP, S, "up", "M", "Manual"),
          R(S, DEP, "cmdb_ci_datacenter", "down", "M", "Manual")],
    trace="Business Application -> Consumes::Consumed by -> Service Instance -> Depends on::Used by -> {L} -> Depends on::Used by -> Data Center / facility equipment -> location"),
 "cmdb_ci_infra_service": dict(note="Legacy class that predates CSDM. Prefer a Service Instance type; migrate existing records.",
    gate="Fail for new records: model as a Service Instance type instead."),
 "cmdb_ci_endpoint": dict(rels=[R("cmdb_ci_service_discovered", DEP, S, "up", "M", "Service Mapping (entry point)"),
          R(S, "Implement End Point To::Implement End Point From", "cmdb_ci_appl", "down", "M", "Service Mapping"),
          R("cmdb_ci_appl", "Use End Point To::Use End Point From", S, "lat", "O", "Service Mapping")],
    source="Service Mapping", trace=TOP.replace("Service Instance", "Mapped Application Service") + "{L} -> Implement End Point To::Implement End Point From -> Application -> Runs on::Runs -> Server",
    stale="Follows the Mapped Application Service recomputation.", conf="Medium",
    note="Created and removed by Service Mapping. Do not create manually except as an entry point."),
 "cmdb_ci_api_gateway": dict(note="Software gateways run on servers; cloud-managed gateways follow the cloud resource pattern instead."),
 # applications
 "cmdb_ci_appl_generic": dict(note="Catch-all class. A high count signals missing classification patterns; reclassify to a product class where one exists."),
 "cmdb_ci_app_server_tomcat_war": via("cmdb_ci_app_server_tomcat", CONT),
 "cmdb_ci_web_site": via("cmdb_ci_web_server", CONT),
 "cmdb_ci_web_application": via("cmdb_ci_app_server", CONT),
 "cmdb_ci_web_service": via("cmdb_ci_app_server", CONT),
 "cmdb_ci_appl_ibm_wmq_queue": via("cmdb_ci_appl_ibm_wmq", CONT),
 "cmdb_ci_windows_service": dict(via="cmdb_ci_win_server", rels=[R(S, RUN, "cmdb_ci_win_server", "up", "M", "Discovery")]),
 "cmdb_ci_unix_daemon": dict(via="cmdb_ci_server", rels=[R(S, RUN, "cmdb_ci_server", "up", "M", "Discovery")]),
 "cmdb_ci_config_file": via("cmdb_ci_appl", CONT),
 "cmdb_ci_spkg": dict(via="cmdb_ci_computer", rels=[R("cmdb_ci_computer", "Software instance record (cmdb_software_instance / cmdb_sam_sw_install)", S, "up", "M", "Discovery / SAM")],
    ident="Independent. Match on name + version (verify identifier entry). One record per software title and version, not per install.",
    dep="Independent", req=["name", "version"], key=["version"],
    orphan="Software package with no install records.", note="Installs are rows in the software instance / installation tables, not CI relationships."),
 "cmdb_ci_ad_domain": dict(down_text="Verify in instance: link to the Domain Controllers that serve the domain."),
 "cmdb_ci_directory_ad_forest": dict(down_text="Verify in instance: link to the AD Domains in the forest."),
 "cmdb_ci_vcenter": dict(rels=[R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"), R(S, RUN, "cmdb_ci_server", "down", "M", "Discovery")],
    trace="Technology Management Offering (virtualisation) -> Dynamic CI Group -> {L} -> Runs on::Runs -> Server; manages vCenter Datacenters, Clusters and ESX Servers",
    csdm="Platform management application: owned through the virtualisation Technology Management Offering."),
 # databases
 "cmdb_ci_database": dict(via="cmdb_ci_db_instance", rels=[R("cmdb_ci_db_instance", CONT, S, "up", "M", "Discovery")]),
 "cmdb_ci_db_catalog": dict(via="cmdb_ci_db_instance", rels=[R("cmdb_ci_db_instance", CONT, S, "up", "M", "Discovery")]),
 "cmdb_ci_db_mssql_catalog": dict(via="cmdb_ci_db_mssql_instance", rels=[R("cmdb_ci_db_mssql_instance", CONT, S, "up", "M", "Discovery")]),
 "cmdb_ci_db_ora_catalog": dict(via="cmdb_ci_db_ora_instance", rels=[R("cmdb_ci_db_ora_instance", CONT, S, "up", "M", "Discovery")]),
 "cmdb_ci_db_mysql_catalog": dict(via="cmdb_ci_db_mysql_instance", rels=[R("cmdb_ci_db_mysql_instance", CONT, S, "up", "M", "Discovery")]),
 "cmdb_ci_db_db2_catalog": dict(via="cmdb_ci_db_db2_instance", rels=[R("cmdb_ci_db_db2_instance", CONT, S, "up", "M", "Discovery")]),
 "cmdb_ci_db_mssql_instance": dict(req_add=["instance_name"], key_add=["instance_name"]),
 "cmdb_ci_db_ora_instance": dict(req_add=["sid"], key_add=["sid"]),
 # compute
 "cmdb_ci_computer": dict(req_add=["os", "os_version"], rec_add=["cpu_count", "cpu_core_count", "ram", "disk_space", "os_domain", "chassis_type"], key_add=["os", "os_version", "cpu_core_count", "ram"]),
 "cmdb_ci_server": dict(req_add=["used_for"], rec_add=["host_name", "classification"], key_add=["host_name", "used_for", "classification"]),
 "cmdb_ci_win_server": dict(key_add=["os_domain"]),
 "cmdb_ci_unclassified_hardware": dict(gate="Fail: holding class. Reclassify to a specific class before acceptance.",
    note="Holding class for devices Discovery could not classify. Target count is zero."),
 "cmdb_ci_incomplete_ip": dict(gate="Fail: holding class. Complete identification and reclassify before acceptance.",
    note="Holding class for devices identified only by IP address. Target count is zero."),
 "cmdb_ci_hyper_v_server": dict(rels=[R("cmdb_ci_hyper_v_instance", REG, S, "up", "M", "Discovery (Hyper-V)"), R(S, LOC, "cmdb_ci_rack", "down", "M", "Manual / DCIM import")]),
 "cmdb_ci_nutanix_host": dict(rels=[R("cmdb_ci_nutanix_vm_instance", REG, S, "up", "M", "Discovery (Nutanix), verify relationship type"), R(S, LOC, "cmdb_ci_rack", "down", "M", "Manual / DCIM import"),
          R("cmdb_ci_nutanix_cluster", MEM, S, "lat", "O", "Discovery (Nutanix)")]),
 "cmdb_ci_cluster_node": dict(via="cmdb_ci_cluster", req=["name", "cluster", "server", "operational_status"], key=["cluster", "server"],
    rels=[R(S, "Reference field: cluster", "cmdb_ci_cluster", "up", "M", "Discovery"), R(S, "Reference field: server", "cmdb_ci_server", "down", "M", "Discovery")],
    down_text=""),
 "cmdb_ci_win_cluster_node": dict(via="cmdb_ci_win_cluster", key=["cluster", "server"],
    rels=[R(S, "Reference field: cluster", "cmdb_ci_win_cluster", "up", "M", "Discovery"), R(S, "Reference field: server", "cmdb_ci_win_server", "down", "M", "Discovery")],
    down_text=""),
 "cmdb_ci_cluster_resource": dict(via="cmdb_ci_cluster", req=["name", "cluster", "operational_status"], key=["cluster"], rels=[R(S, "Reference field: cluster", "cmdb_ci_cluster", "up", "M", "Discovery")]),
 "cmdb_ci_cluster_vip": dict(via="cmdb_ci_cluster", req=["name", "cluster", "ip_address", "operational_status"], key=["cluster", "ip_address"], rels=[R(S, "Reference field: cluster", "cmdb_ci_cluster", "up", "M", "Discovery")]),
 "cmdb_ci_win_cluster": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Service Mapping / manual"), R("cmdb_ci_win_cluster_node", "Reference field: cluster", S, "down", "M", "Discovery")]),
 "cmdb_ci_gpu": via("cmdb_ci_computer"),
 "cmdb_ci_memory_module": via("cmdb_ci_computer"),
 # network
 "cmdb_ci_lb_service": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Service Mapping"), R(S, "Reference field: load_balancer", "cmdb_ci_lb", "down", "M", "Discovery"),
          R(S, USE, "cmdb_ci_lb_pool", "lat", "O", "Discovery")]),
 "cmdb_ci_lb_pool": dict(req=["name", "load_balancer", "operational_status"], key=["load_balancer"],
    rels=[R("cmdb_ci_lb_service", USE, S, "up", "M", "Discovery"), R(S, "Reference field: load_balancer", "cmdb_ci_lb", "down", "M", "Discovery"),
          R(S, MEM, "cmdb_ci_lb_pool_member", "lat", "O", "Discovery")]),
 "cmdb_ci_lb_pool_member": via("cmdb_ci_lb_pool", MEM),
 "cmdb_ci_ip_address": dict(via="cmdb_ci_network_adapter", req=["name", "ip_address", "nic"], rec=["netmask"], key=["ip_address", "nic"],
    rels=[R(S, "Reference field: nic", "cmdb_ci_network_adapter", "up", "M", "Discovery")]),
 "cmdb_ci_network_adapter": dict(via="cmdb_ci_hardware", req=["name", "mac_address", "cmdb_ci"], rec=["ip_address", "netmask"], key=["mac_address", "cmdb_ci"],
    rels=[R(S, "Reference field: cmdb_ci", "cmdb_ci_hardware", "up", "M", "Discovery")],
    note="Used as a lookup table by the Hardware identification rule (ip_address + mac_address)."),
 "cmdb_ci_port": via("cmdb_ci_netgear"),
 "cmdb_ci_ip_network": dict(req=["name", "subnet", "operational_status"], key=["subnet"], down_text="Verify in instance: relationship to the router / switch that serves the subnet."),
 "cmdb_ci_circuit": dict(rels=[R("cmdb_ci_connection_service_instance", DEP, S, "up", "M", "Manual")], down_text="Provider and termination sites: verify fields and relationships to the terminating network devices."),
 "cmdb_ci_network_circuit": dict(rels=[R("cmdb_ci_connection_service_instance", DEP, S, "up", "M", "Manual")]),
 "cmdb_ci_network_link": dict(rels=[R("cmdb_ci_connection_service_instance", DEP, S, "up", "M", "Manual")]),
 "cmdb_ci_ip_phone": dict(note="Shared or unassigned phones: use location and department in place of assigned_to."),
 # storage
 "cmdb_ci_storage_controller": via("cmdb_ci_storage_device"),
 "cmdb_ci_storage_pool": via("cmdb_ci_storage_device"),
 "cmdb_ci_storage_volume": dict(via="cmdb_ci_storage_pool", rec=["size_bytes"], rels=[R("cmdb_ci_storage_pool", VERIFY_REL, S, "up", "M", "Discovery")]),
 "cmdb_ci_storage_fileshare": via("cmdb_ci_storage_device"),
 "cmdb_ci_storage_hba": via("cmdb_ci_server"),
 "cmdb_ci_san_fabric": via("cmdb_ci_san"),
 "cmdb_ci_san_zone": via("cmdb_ci_san_fabric"),
 "cmdb_ci_disk": dict(via="cmdb_ci_computer", req=["name", "computer"], rec=["size_bytes"], key=["computer", "size_bytes"], rels=[R(S, "Reference field: computer", "cmdb_ci_computer", "up", "M", "Discovery")]),
 "cmdb_ci_file_system": dict(via="cmdb_ci_computer", req=["name", "computer", "mount_point"], rec=["size_bytes", "free_space_bytes"], key=["computer", "mount_point"],
    rels=[R(S, "Reference field: computer", "cmdb_ci_computer", "up", "M", "Discovery")]),
 "cmdb_ci_nas_file_system": dict(via="cmdb_ci_computer", rels=[R(S, "Reference field: computer", "cmdb_ci_computer", "up", "M", "Discovery")]),
 "cmdb_ci_datastore": via("cmdb_ci_esx_server"),
 "cmdb_ci_netapp_svm": via("cmdb_ci_netapp_cdot"),
 "cmdb_ci_netapp_volume": via("cmdb_ci_netapp_svm"),
 # virtualisation
 "cmdb_ci_vm_instance": dict(req_add=["state"], rec_add=["cpus", "memory", "disks_size", "nics"], key_add=["state", "cpus", "memory"]),
 "cmdb_ci_vmware_instance": dict(key_add=["Verify in instance: vCenter reference fields (vcenter_ref, vcenter_uuid)"],
    rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery"), R(S, REG, "cmdb_ci_esx_server", "down", "M", "Discovery (vCenter)")]),
 "cmdb_ci_hyper_v_instance": dict(rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery"), R(S, REG, "cmdb_ci_hyper_v_server", "down", "M", "Discovery (Hyper-V)")]),
 "cmdb_ci_nutanix_vm_instance": dict(rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery"), R(S, REG, "cmdb_ci_nutanix_host", "down", "M", "Discovery (Nutanix), verify relationship type")]),
 "cmdb_ci_ec2_instance": dict(rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Cloud discovery"), R(S, HOST, "cmdb_ci_aws_datacenter", "down", "M", "Cloud discovery / Service Graph Connector for AWS")],
    trace=TOP + "Application -> Runs on::Runs -> Server -> Virtualized by::Virtualizes -> {L} -> Hosted on::Hosts -> AWS Datacenter -> Hosted on::Hosts -> Cloud Service Account"),
 "cmdb_ci_lpar_instance": dict(rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery"), R(S, REG, "cmdb_ci_hmc_server", "down", "M", "Discovery (HMC), verify relationship type")]),
 "cmdb_ci_kvm_vm_instance": dict(rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery")], down_text="Verify in instance: relationship to the KVM host."),
 "cmdb_ci_solaris_instance": dict(rels=[R("cmdb_ci_server", VIRT, S, "up", "M", "Discovery")], down_text="Verify in instance: relationship to the Solaris global zone / host."),
 "cmdb_ci_vcenter_datacenter": dict(rels=[R(S, CONT, "cmdb_ci_vcenter_cluster", "up", "M", "Discovery (vCenter)"), R(S, "Reference field: vcenter_ref (verify)", "cmdb_ci_vcenter", "down", "M", "Discovery (vCenter)")],
    up_text="", note="Some connectors model the vCenter Datacenter as a logical datacenter hosted on a Cloud Service Account. Confirm which pattern the instance uses."),
 "cmdb_ci_vcenter_cluster": dict(rels=[R(S, MEM, "cmdb_ci_esx_server", "up", "M", "Discovery (vCenter)"), R("cmdb_ci_vcenter_datacenter", CONT, S, "down", "M", "Discovery (vCenter)")], up_text=""),
 "cmdb_ci_hyper_v_cluster": dict(rels=[R(S, MEM, "cmdb_ci_hyper_v_server", "up", "M", "Discovery (Hyper-V)")], up_text="", down_text="Verify in instance: link to the Hyper-V management server.",
    trace="Business Application -> Service Instance -> Application -> Server -> VM Instance -> Hyper-V Server -> {L} -> management server"),
 "cmdb_ci_hyper_v_network": dict(rels=[], down_text="Verify in instance: link to the Hyper-V Server that owns the virtual network.",
    trace="Business Application -> Service Instance -> Application -> Server -> VM Instance -> {L} -> Hyper-V Server"),
 "cmdb_ci_nutanix_cluster": dict(rels=[R(S, MEM, "cmdb_ci_nutanix_host", "up", "M", "Discovery (Nutanix)")], up_text="", down_text="Verify in instance: link to Prism Central / management plane.",
    trace="Business Application -> Service Instance -> Application -> Server -> VM Instance -> Nutanix Host -> {L} -> management plane",
    key=["Verify in instance: cluster identifier fields"]),
 "cmdb_ci_kvm": dict(rels=[], down_text="Verify in instance: link to the host server.", key=["Verify in instance: class-specific identifiers"],
    trace="Business Application -> Service Instance -> Application -> Server -> VM Instance -> {L} -> host Server"),
 "cmdb_ci_vm_template": dict(rels=[], down_text="Verify in instance: link to the vCenter Datacenter / logical datacenter that holds the template.",
    trace="Business Application -> Service Instance -> VM Instance -> (provisioned from) -> {L} -> datacenter"),
 "cmdb_ci_vmware_template": dict(rels=[R("cmdb_ci_vcenter_datacenter", CONT, S, "down", "M", "Discovery (vCenter)")],
    trace="Business Application -> Service Instance -> VM Instance -> (provisioned from) -> {L} -> VMware vCenter Datacenter"),
 "cmdb_ci_virtual_desktop": dict(note="Parent class and identification to be confirmed; persistent desktops follow the end-user pattern, pooled desktops should be governed at pool level."),
 # cloud
 "cmdb_ci_aws_datacenter": dict(rels=[R("cmdb_ci_ec2_instance", HOST, S, "up", "M", "Cloud discovery / Service Graph Connector for AWS"), R(S, HOST, "cmdb_ci_cloud_service_account", "down", "M", "Cloud discovery / Service Graph Connector for AWS")]),
 "cmdb_ci_azure_datacenter": dict(rels=[R("cmdb_ci_vm_instance", HOST, S, "up", "M", "Cloud discovery / Service Graph Connector for Azure"), R(S, HOST, "cmdb_ci_cloud_service_account", "down", "M", "Cloud discovery / Service Graph Connector for Azure"),
          R(S, CONT, "cmdb_ci_resource_group", "lat", "O", "Cloud discovery / Service Graph Connector for Azure")]),
 "cmdb_ci_resource_group": dict(rels=[R(S, CONT, "cmdb_ci_cmp_resource", "up", "O", "Cloud discovery / Service Graph Connector for Azure"),
          R("cmdb_ci_azure_datacenter", CONT, S, "down", "M", "Cloud discovery / Service Graph Connector for Azure")],
    trace="Business Application -> Service Instance -> Azure resource -> (grouped by) -> {L} -> Contains::Contained by (child of) -> Azure Datacenter -> Hosted on::Hosts -> Cloud Service Account",
    host="Containment: Azure Datacenter Contains::Contained by {L}."),
 "cmdb_ci_cmp_resource": dict(note="Generic parent for cloud resources. Prefer the specific resource class."),
 "cmdb_ci_nic": via("cmdb_ci_vm_instance", by="Cloud discovery"),
 "cmdb_ci_cloud_ip_address": via("cmdb_ci_nic", by="Cloud discovery"),
 "cmdb_ci_network_acl_rule": via("cmdb_ci_network_acl", by="Cloud discovery"),
 "cmdb_ci_cloud_database": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "M", "Tag-based service mapping / manual"), R("cmdb_ci_data_service_instance", DEP, S, "up", "O", "Manual"),
          R(S, HOST, "cmdb_ci_logical_datacenter", "down", "M", "Cloud discovery / Service Graph Connector")]),
 "cmdb_ci_dns_domain_info": dict(source="Cloud discovery / DNS integration"),
 "cmdb_ci_dns_resource_record": dict(source="Cloud discovery / DNS integration"),
 # containers
 "cmdb_ci_kubernetes_namespace": dict(rels=[R("cmdb_ci_service_auto", DEP, S, "up", "O", "Tag-based service mapping (labels)"), R("cmdb_ci_kubernetes_cluster", CONT, S, "down", "M", "Kubernetes discovery")],
    trace=TOP + "Kubernetes workload -> {L} -> Contains::Contained by (child of) -> Kubernetes Cluster -> " + CLOUD_TAIL),
 "cmdb_ci_kubernetes_node": dict(rels=[R("cmdb_ci_kubernetes_pod", RUN, S, "up", "M", "Kubernetes discovery"), R("cmdb_ci_kubernetes_cluster", CONT, S, "down", "M", "Kubernetes discovery")],
    trace=TOP + "Kubernetes workload -> Pod -> Runs on::Runs -> {L} -> Kubernetes Cluster -> " + CLOUD_TAIL + " (node also resolves to a Server / VM Instance: verify)",
    stale="7 days without discovery update."),
 "cmdb_ci_kubernetes_node_pool": dict(rels=[R("cmdb_ci_kubernetes_cluster", CONT, S, "down", "M", "Cloud discovery / Kubernetes discovery")],
    up_text="Inherits context from the nodes and workloads that run in the pool.", stale="7 days without discovery update."),
 "cmdb_ci_kubernetes_pod": dict(rels=[R("cmdb_ci_kubernetes_namespace", CONT, S, "up", "M", "Kubernetes discovery"), R(S, RUN, "cmdb_ci_kubernetes_node", "down", "M", "Kubernetes discovery")],
    trace=TOP + "Kubernetes workload -> {L} -> Runs on::Runs -> Kubernetes Node -> Kubernetes Cluster -> " + CLOUD_TAIL,
    stale="1 to 3 days without discovery update. Govern the workload, not individual pods.", gate="Informational: accept if namespace and node resolve."),
 "cmdb_ci_docker_engine": dict(rels=[R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"), R(S, RUN, "cmdb_ci_server", "down", "M", "Discovery")],
    csdm="Container runtime: owned through the container platform Technology Management Offering."),
 "cmdb_ci_oslv_engine": dict(rels=[R("cmdb_ci_query_based_service", ASSOC, S, "up", "M", "CMDB Group saved query"), R(S, RUN, "cmdb_ci_server", "down", "M", "Discovery")],
    csdm="Container runtime: owned through the container platform Technology Management Offering."),
 "cmdb_ci_docker_image": dict(rels=[R(S, "Instantiates::Instantiated by", "cmdb_ci_docker", "up", "O", "Discovery")], down_text="Verify in instance: link to the registry / engine that holds the image.",
    trace="Business Application -> Service Instance -> workload -> Docker Container -> (instance of) -> {L} -> registry / engine",
    orphan="Image not instantiated by any container.", stale="30 days without discovery update."),
 "cmdb_ci_oslv_image": dict(rels=[R(S, "Instantiates::Instantiated by", "cmdb_ci_oslv_container", "up", "O", "Discovery")], down_text="Verify in instance: link to the registry / engine that holds the image.",
    trace="Business Application -> Service Instance -> workload -> Container -> (instance of) -> {L} -> registry / engine",
    orphan="Image not instantiated by any container.", stale="30 days without discovery update."),
 # facilities
 "cmdb_ci_datacenter": dict(rels=[R("cmdb_ci_facility_service_instance", DEP, S, "up", "O", "Manual"), R("cmdb_ci_computer_room", LOC, S, "up", "M", "Manual / DCIM import")]),
 "cmdb_ci_zone": dict(rels=[R(S, LOC, "cmdb_ci_datacenter", "down", "M", "Manual / DCIM import")], up_text="Inherits context from the racks and rooms in the zone.", down_text=""),
 "cmdb_ci_computer_room": dict(rels=[R("cmdb_ci_rack", LOC, S, "up", "M", "Manual / DCIM import"), R(S, LOC, "cmdb_ci_datacenter", "down", "M", "Manual / DCIM import")], down_text=""),
 "cmdb_ci_rack": dict(req=["name", "location", "rack_units", "operational_status"], key=["location", "rack_units"],
    rels=[R("cmdb_ci_server", LOC, S, "up", "M", "Manual / DCIM import"), R(S, LOC, "cmdb_ci_computer_room", "down", "M", "Manual / DCIM import")], down_text="",
    trace="Business Application -> Service Instance -> Application -> Server -> Located in::Houses -> {L} -> Located in::Houses -> Computer Room -> Data Center -> location (Foundation)"),
}
