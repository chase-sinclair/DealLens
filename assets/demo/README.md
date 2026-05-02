# DealLens Demo Screenshot Assets

Use this folder to store screenshots for the DealLens product demo video.

The demo should use real screenshots where available and polished placeholder UI mocks where screenshots are missing. Screenshots should be clean, cropped, and free of API keys, internal IDs, unrelated browser tabs, bookmarks, private account info, or confidential-looking data.

## Naming Convention

Use lowercase, hyphenated filenames. Prefer `.png`.

## Core Screenshot Assets

| File | Purpose | Notes |
|---|---|---|
| `northstar-cim-pdf.png` | Northstar CIM source document | Use the PDF cover page or a clean company overview page. |
| `drive-cim-intake.png` | Google Drive intake folder | Show `CIM Intake` with the Northstar PDF visible. |
| `zapier-cim-intake-overview.png` | Zapier workflow overview | Show Zap 1 with key steps visible: Drive, PDF.co, OpenAI, Airtable, Slack, Google Docs. |
| `airtable-deals-northstar-row.png` | Airtable Deals row | Show the populated Northstar record with core fields and recommended next step. |
| `airtable-executive-dashboard.png` | Airtable Executive Dashboard | Show KPI cards, charts, deal prioritization, and workflow health if possible. |
| `airtable-deal-review-summary.png` | Airtable Deal Review interface | Show Northstar summary, metrics, risks, diligence, and criteria if possible. |
| `slack-deallens-alert-northstar.png` | Slack alert | Show the formatted DealLens alert for Northstar. |
| `google-docs-northstar-ic-memo.png` | Generated IC memo | Show the top of the generated Google Docs memo. |
| `airtable-workflow-runs-northstar.png` | Workflow run logging | Show statuses, processing duration, time saved, and records created. |
| `airtable-multiple-deals.png` | Scale/repeatability proof | Show Northstar, MedAxis, and BrightCart in Airtable. |

## Optional Supporting Assets

| File | Purpose | Notes |
|---|---|---|
| `airtable-deals-memo-link.png` | Memo link write-back | Only needed if the main Deals row screenshot does not show the Memo Link field. |
| `airtable-investment-criteria-northstar.png` | Investment Criteria rows | Optional close-up of scoring criteria for Northstar. |
| `drive-multiple-cims.png` | Multiple CIM files | Optional scale ending visual. |
| `drive-generated-memos.png` | Multiple generated memo docs | Optional scale ending visual. |
| `pdfco-extraction-output.png` | PDF.co extracted text | Optional; Codex can mock this if the real screen is noisy. |
| `openai-structured-output.png` | Structured JSON output | Optional; Codex can mock this as a clean animated JSON panel. |

## Multiple Screenshots Per Scene

Yes, a scene can use multiple screenshots.

Use this naming pattern when one scene needs multiple images:

```text
scene-name-01.png
scene-name-02.png
scene-name-03.png
```

Examples:

```text
airtable-deal-review-01-summary.png
airtable-deal-review-02-financials.png
airtable-deal-review-03-risks-diligence.png

zapier-cim-intake-01-overview.png
zapier-cim-intake-02-run-history.png

workflow-writeback-01-workflow-runs.png
workflow-writeback-02-memo-link.png
```

For multi-screenshot scenes, Codex should use smooth pans, zooms, crossfades, or side-by-side layouts instead of trying to show everything at once.

## Codex Usage Rule

Codex should:

1. Use real screenshots from this folder when present.
2. Use polished placeholder UI mocks when screenshots are missing.
3. Never block video generation because an asset is missing.
4. Keep placeholders easy to replace later by referencing the same expected filename.
5. Treat Airtable as the hero product surface.
6. Treat Zapier, PDF.co, OpenAI, Slack, Google Docs, and Google Drive as supporting workflow systems.

## Product Narrative

Primary narrative:

```text
Document in → AI workflow automation → review-ready PE deal workspace out.
```

Main company:

```text
Northstar Field Services
```

MedAxis and BrightCart should only appear near the end as proof that the workflow generalized across multiple synthetic CIMs.
