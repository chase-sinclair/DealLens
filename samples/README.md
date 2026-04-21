# Synthetic CIM Dataset

Use only synthetic or public non-confidential source materials.

Phase 2 sample set:

1. `cims/northstar-field-services.md` - strong-fit B2B services platform.
2. `cims/medaxis-revenue-solutions.md` - medium-fit healthcare services deal with missing data.
3. `cims/brightcart-consumer-goods.md` - poor-fit consumer deal with clear pass rationale.

Generated PDFs:

1. `pdfs/northstar-field-services.pdf`
2. `pdfs/medaxis-revenue-solutions.pdf`
3. `pdfs/brightcart-consumer-goods.pdf`

Benchmark expectations:

```text
expected-outputs.md
```

Each sample should have expected outputs for QA:

- Company profile
- Financial metrics
- Key risks
- Missing fields
- Diligence questions
- Expected fit score range
- Recommended next step

Regenerate PDFs after editing source markdown:

```powershell
python samples\generate_sample_pdfs.py
```
