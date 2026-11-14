# CI Class Atlas

A searchable reference data model for ServiceNow CMDB CI classes on CSDM 5.0, organised by the three C's of CMDB Health: completeness, correctness and compliance.

**Site:** https://kmrreddy111.github.io/ci-class-atlas/

## What is here

| Path | Contents |
|---|---|
| `index.html`, `data.js` | The static site. Search by description or table name; each class opens as a three C board or as the classic workbook row. |
| `workbook/CMDB_Class_Data_Model_CSDM5.xlsx` | The same model as an Excel workbook: 322 classes, relationship matrix, reference patterns, attribute dictionary, open items. |
| `source/model.py`, `source/build.py` | The model as data and the script that generates the workbook and `data.js`. |

## Status: draft

This model has **not been validated against a live instance**. Every class carries a confidence marker, and anything labelled "Verify in instance" must be confirmed in CI Class Manager before it is relied on. Staleness durations, certification owners and required attributes are proposals, not platform defaults.

## Rebuild

```
cd source
pip install openpyxl
python build.py ../workbook/CMDB_Class_Data_Model_CSDM5.xlsx data.json
python -c "open('../data.js','w').write('window.DATA='+open('data.json').read()+';')"
```

## Notice

Independent community reference. Not affiliated with or endorsed by ServiceNow. ServiceNow, CSDM and related names are trademarks of ServiceNow, Inc.

## Licence

Code is licensed under Apache 2.0 (`LICENSE`). The data model and workbook are licensed under CC BY 4.0 (`LICENSE-DATA.md`).
