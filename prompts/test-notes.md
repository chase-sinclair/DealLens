# Prompt Test Notes

Phase 3 prompt testing should use the three workflow input PDFs in `samples/pdfs`.

## Test Cases

| CIM | Expected Recommended Next Step | Expected Fit Score Range | Notes |
|---|---|---:|---|
| Northstar Field Services | Proceed to initial review | 78-88 | Strong B2B services platform. Northstar PDF extraction includes citation artifacts; prompts must ignore them. |
| MedAxis Revenue Solutions | Request more information | 66-76 | Medium-fit healthcare services deal with missing NRR, renewal, and concentration details. |
| BrightCart Consumer Goods | Pass | 35-50 | Low-fit consumer deal with declining revenue, low margin, and missing channel/customer data. |

## Validation Checklist

- [x] Output is valid JSON.
- [x] No markdown code fences are included.
- [x] No citation artifacts appear in extracted Airtable fields.
- [x] FY2025 Adjusted EBITDA is used for the `deal.ebitda` field.
- [x] FY2025 Adjusted EBITDA Margin is used for `deal.ebitda_margin`.
- [x] Missing fields are explicit and specific.
- [x] Risks are deal-specific.
- [x] Diligence questions are deal-specific.
- [x] Recommended next step matches expected routing.
- [x] Overall fit score is within expected range or rationale explains variance.

## Live Test Results

Test command:

```powershell
python prompts\test_extraction_prompt.py <sample-name>
```

Results:

| CIM | Actual Recommended Next Step | Actual Fit Score | Citation Artifacts In JSON | Result |
|---|---|---:|---|---|
| Northstar Field Services | Proceed to initial review | 80 | No | Pass |
| MedAxis Revenue Solutions | Request more information | 70 | No | Pass |
| BrightCart Consumer Goods | Pass | 40 | No | Pass |

Generated test outputs are written to `outputs/prompt-tests/`, which is ignored by Git.
