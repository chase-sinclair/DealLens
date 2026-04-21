# Synthetic CIM Dataset

Use only synthetic or public non-confidential source materials.

Phase 2 sample set:

1. `cims/northstar-field-services.md` - strong-fit B2B services platform.
2. `cims/medaxis-revenue-solutions.md` - medium-fit healthcare services deal with missing data.
3. `cims/brightcart-consumer-goods.md` - poor-fit consumer deal with clear pass rationale.

Sample PDFs:

1. `pdfs/northstar-field-services.pdf` - user-supplied designed PDF used as the workflow input artifact.
2. `pdfs/medaxis-revenue-solutions.pdf` - user-supplied designed PDF used as the workflow input artifact.
3. `pdfs/brightcart-consumer-goods.pdf`

The Northstar and MedAxis Markdown sources remain as clean text references, but the workflow inputs for those samples are the PDFs in `samples/pdfs`.

Extraction note:

```text
The current Northstar PDF text extraction includes citation artifacts such as [cite: 238-239].
Phase 3 prompts should instruct OpenAI to ignore citation markers and never map them into Airtable fields.
The current MedAxis PDF extracts cleanly without citation artifacts.
```

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

Regenerate generated PDFs after editing source markdown:

```powershell
python samples\generate_sample_pdfs.py
```

The generator skips user-supplied Northstar and MedAxis PDFs if they already exist.
