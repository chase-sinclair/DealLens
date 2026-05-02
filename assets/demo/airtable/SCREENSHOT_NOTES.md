# Airtable Screenshot Notes

Screenshots received for the Deals table showing the full Northstar Field Services deal record across three horizontal sections, the two main Airtable interfaces, and the Workflow Runs table.

## Files to add

### Deals table screenshots

```text
airtable-deals-01-core-fields.png
airtable-deals-02-business-model-fields.png
airtable-deals-03-scoring-next-step.png
```

### Airtable interface screenshots

```text
airtable-executive-dashboard.png
airtable-deal-review-interface.png
```

### Workflow Runs screenshots

```text
airtable-workflow-runs-01-statuses.png
airtable-workflow-runs-02-impact-metrics.png
```

## Deals table scene

Use these three screenshots together as a multi-screenshot scene rather than trying to show the entire Airtable table at once.

Recommended visual treatment:

1. Start with `airtable-deals-01-core-fields.png` to show the populated Northstar deal record with core extracted fields:
   - Company Name
   - Sector
   - Subsector
   - Headquarters
   - Founded Year
   - Ownership / Seller Type
   - Revenue
   - Revenue Growth
   - EBITDA

2. Crossfade or slide to `airtable-deals-02-business-model-fields.png` to show operational and customer context:
   - EBITDA Margin
   - Business Model
   - Revenue Model
   - Customer Segments
   - Customer Concentration
   - Geographic Footprint
   - Employee Count
   - Transaction Type

3. Crossfade or slide to `airtable-deals-03-scoring-next-step.png` to show review-readiness and AI scoring:
   - Banker / Advisor
   - Process Deadline
   - Investment Highlights
   - Growth Opportunities
   - Key Risks Summary
   - Fit Score
   - Data Completeness
   - Recommended Next Step

## Executive Dashboard scene

Use `airtable-executive-dashboard.png` as the main portfolio-level product proof.

What it shows:

- Total Deals: 3
- Average Fit Score: 67
- Average Data Completeness: 67%
- Open Diligence Questions: 3
- Deal Pipeline by Recommendation donut chart
- Deal Prioritization Matrix
- Deal Table with Northstar, BrightCart, and MedAxis
- Workflow Health section with run status and time saved

Recommended visual treatment:

1. Show the full dashboard briefly to establish the interface.
2. Zoom into KPI cards.
3. Pan to the recommendation chart and prioritization matrix.
4. Zoom into the Deal Table to show all three processed CIMs.
5. End on Workflow Health to show operational tracking.

Recommended callouts:

```text
3 CIMs processed
Portfolio-level review dashboard
Pipeline recommendations visible
Workflow health tracked automatically
```

## Deal Review interface scene

Use `airtable-deal-review-interface.png` as the single-deal analyst review hero screen.

What it shows:

- Northstar Field Services selected in the left panel
- Deal summary fields
- Financial Metrics
- Investment Criteria
- Risks
- Diligence Questions
- BrightCart and MedAxis also available in the left-side deal list

Recommended visual treatment:

1. Show the full Deal Review interface.
2. Zoom into the Northstar title and summary fields.
3. Pan through Financial Metrics and Investment Criteria.
4. Pan through Risks and Diligence Questions.
5. Add a final callout that this is the review-ready workspace created from the CIM.

Recommended callouts:

```text
Review-ready deal workspace
Financial metrics linked to the deal
Risks and diligence questions generated
Investment criteria created for explainable review
```

## Workflow Runs scene

Use the two Workflow Runs screenshots together as proof that the product tracks automation status, records created, and estimated manual effort saved.

### `airtable-workflow-runs-01-statuses.png`

Shows:

- Run ID
- Deal
- CIM Document
- Upload Time
- Processing Completed Time
- Processing Duration
- Extraction Status
- OpenAI Status
- Airtable Write Status
- Memo Generation Status
- Slack Notification Status
- Fields Extracted Count

### `airtable-workflow-runs-02-impact-metrics.png`

Shows:

- Missing Fields Count
- Risks Created Count
- Diligence Questions Created Count
- Estimated Manual Minutes Saved
- Error Message

Recommended visual treatment:

1. Show the first Workflow Runs screenshot and highlight successful status fields.
2. Slide or pan to the second screenshot.
3. Highlight fields extracted, risks created, diligence questions created, and estimated manual minutes saved.
4. Keep this short; it supports the impact story but should not distract from the main Airtable interfaces.

Recommended callouts:

```text
Workflow status logged automatically
Extraction, OpenAI, Airtable, memo, and Slack steps tracked
Fields extracted: 30
Risks created: 5
Estimated manual minutes saved: 45
```

## Recommended callouts for Deals table

Use short callouts over the screenshots:

```text
Structured deal record created
Financial metrics normalized
Fit score: 85
Data completeness: 80%
Recommended next step: Proceed to initial review
```

## Direction for Codex / HyperFrames

Airtable is the hero product surface. Treat the Deals table as proof that the CIM was converted into structured deal data, the Executive Dashboard as proof of portfolio-level visibility, the Deal Review interface as the final analyst-facing product workspace, and the Workflow Runs table as proof of operational tracking and measurable time savings.

Do not show the entire table zoomed out if it makes text unreadable. Use horizontal pan, slide transitions, focused zooms, and callouts across the provided screenshots.
