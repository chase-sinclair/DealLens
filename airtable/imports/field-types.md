# Airtable Field Type Guide

Use this after importing CSVs into a clean Airtable base. Airtable will infer many fields as text; adjust the important ones after import.

## Deals

| Field | Type |
|---|---|
| Company Name | Single line text |
| Sector | Single select |
| Subsector | Single line text |
| Headquarters | Single line text |
| Founded Year | Number |
| Ownership / Seller Type | Single select |
| Revenue | Currency |
| Revenue Growth | Percent |
| EBITDA | Currency |
| EBITDA Margin | Percent |
| Business Model | Long text |
| Revenue Model | Long text |
| Customer Segments | Long text |
| Customer Concentration | Long text |
| Geographic Footprint | Long text |
| Employee Count | Number |
| Transaction Type | Single select |
| Banker / Advisor | Single line text |
| Process Deadline | Date |
| Investment Highlights | Long text |
| Growth Opportunities | Long text |
| Key Risks Summary | Long text |
| Missing Fields | Long text |
| Fit Score | Number |
| Data Completeness Score | Percent |
| Recommended Next Step | Single select |
| Deal Status | Single select |
| Memo Link | URL |
| CIM Document Link | URL |
| Date Processed | Date |
| Analyst Owner | Collaborator or single line text |
| Reviewer Notes | Long text |

## CIM Documents

| Field | Type |
|---|---|
| Document Name | Single line text |
| Deal | Link to Deals |
| Google Drive File Link | URL |
| File Upload Time | Date with time |
| Extraction Status | Single select |
| Extraction Tool | Single select |
| Raw Text Available | Checkbox or single select |
| Extraction Error | Long text |
| Page Count | Number |
| Date Processed | Date |

## Financial Metrics

| Field | Type |
|---|---|
| Metric ID | Single line text primary field |
| Deal | Link to Deals |
| Period | Single line text |
| Revenue | Currency |
| Revenue Growth | Percent |
| Gross Margin | Percent |
| EBITDA | Currency |
| EBITDA Margin | Percent |
| Capex | Currency |
| Net Working Capital | Currency |
| Free Cash Flow | Currency |
| Notes | Long text |

## Risks

| Field | Type |
|---|---|
| Risk ID | Single line text primary field |
| Deal | Link to Deals |
| Risk Category | Single select |
| Risk Description | Long text |
| Severity | Single select |
| Evidence / Rationale | Long text |
| Reviewer Status | Single select |
| Owner | Collaborator or single line text |
| Follow-Up Needed | Checkbox |

## Diligence Questions

| Field | Type |
|---|---|
| Question ID | Single line text primary field |
| Deal | Link to Deals |
| Question | Long text |
| Category | Single select |
| Priority | Single select |
| Owner | Collaborator or single line text |
| Status | Single select |
| Due Date | Date |
| Source / Rationale | Long text |

## Workflow Runs

| Field | Type |
|---|---|
| Run ID | Single line text primary field |
| Deal | Link to Deals |
| CIM Document | Link to CIM Documents |
| Upload Time | Date with time |
| Processing Completed Time | Date with time |
| Processing Duration Minutes | Number |
| Extraction Status | Single select |
| OpenAI Status | Single select |
| Airtable Write Status | Single select |
| Memo Generation Status | Single select |
| Slack Notification Status | Single select |
| Fields Extracted Count | Number |
| Missing Fields Count | Number |
| Risks Created Count | Number |
| Diligence Questions Created Count | Number |
| Estimated Manual Minutes Saved | Number |
| Error Message | Long text |

## Investment Criteria

| Field | Type |
|---|---|
| Criterion | Single line text primary field |
| Description | Long text |
| Weight | Number |
| Target / Threshold | Single line text |
| Scoring Notes | Long text |

## Review Notes

| Field | Type |
|---|---|
| Review Note ID | Single line text primary field |
| Deal | Link to Deals |
| Reviewer | Collaborator or single line text |
| Review Stage | Single select |
| Decision | Single select |
| Main Concern | Long text |
| Follow-Up Request | Long text |
| Notes | Long text |
| Review Date | Date |

## Select Options

### Common Status Options

- Pending
- Complete
- Failed

### Risk Severity

- Low
- Medium
- High

### Diligence Priority

- Low
- Medium
- High

### Diligence Status

- Open
- In Progress
- Complete
- Blocked

### Deal Status

- New
- Needs Analyst Review
- In Review
- Request Info
- IC Ready
- Passed
- Archived
