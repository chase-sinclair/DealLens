# DealLens - Build Playbook

## Project Name

DealLens

Full project title:

```text
DealLens: CIM Intelligence Pipeline for Private Equity
```

## Project Goal

Build a portfolio-ready private equity automation product that identifies a manual CIM screening process, automates the highest-friction review steps, and surfaces structured deal intelligence in a polished analyst workspace.

DealLens now automates first-pass CIM review end to end. A CIM PDF is uploaded to Google Drive, processed through Zapier, extracted with PDF.co, structured with OpenAI, written into Airtable, expanded into risks, diligence questions, workflow logs, and investment criteria, summarized in a Google Docs IC memo, and announced in Slack.

## Positioning

Recruiter-facing summary:

> Built a three-Zap CIM review pipeline using OpenAI for document intelligence, Airtable as a PE deal operating system, Google Docs for first-pass IC memo generation, and Slack for analyst alerts. The workflow converts unstructured CIM PDFs into structured deal records, linked financial metrics, risks, diligence questions, workflow run logs, investment criteria, and dashboards measuring completeness, time saved, and review readiness.

## Locked Stack

| Tool | Role |
|---|---|
| Google Drive | CIM intake folder, archive, and memo storage |
| Zapier | Main multi-Zap orchestration layer |
| PDF.co | PDF text extraction |
| OpenAI API | Structured extraction, scoring, risks, diligence questions, memo drafting |
| Airtable | Deal operating system, review workspace, dashboards, workflow metrics |
| Google Docs | First-pass investment memo output |
| Slack | Analyst alerts and workflow notifications |

Do not use Supabase or Looker Studio for this build.

## Core Workflow

### Zap 1 - CIM Intake

1. User uploads a CIM PDF to the Google Drive intake folder.
2. Zapier detects the new file.
3. PDF.co extracts raw text.
4. OpenAI converts extracted text into structured deal intelligence.
5. Code by Zapier normalizes percent and metric fields for Airtable.
6. Zapier creates or updates Airtable records for Deals, CIM Documents, Financial Metrics, and Workflow Runs.
7. Zapier posts a Slack alert with key deal context.
8. Zapier creates a Google Docs first-pass IC memo.
9. Zapier writes the memo link back to the Deal record.
10. Zapier loops through and creates linked Risk records.

### Zap 2 - Diligence Builder

1. Airtable watches the `Needs Diligence Questions` view in Deals.
2. OpenAI generates deal-specific diligence questions from structured deal context.
3. Zapier creates a Workflow Runs record for the diligence generation event.
4. Zapier loops through and creates linked Diligence Question records.

### Zap 3 - Investment Criteria Builder

1. Airtable watches the `Needs Investment Criteria` view in Deals.
2. Code by Zapier derives criterion rows from deal-level fit, margin, growth, and completeness data.
3. Zapier loops through and creates linked Investment Criteria records.

## Airtable Application Design

### Base

Base name:

```text
DealLens
```

### Tables

#### Deals

Primary table for one record per target company or CIM.

Core fields in production:

- Company Name
- Sector
- Subsector
- Headquarters
- Founded Year
- Ownership / Seller Type
- Revenue
- Revenue Growth
- EBITDA
- EBITDA Margin
- Business Model
- Revenue Model
- Customer Segments
- Customer Concentration
- Geographic Footprint
- Employee Count
- Transaction Type
- Banker / Advisor
- Process Deadline
- Investment Highlights
- Growth Opportunities
- Key Risks Summary
- Fit Score
- Data Completeness Score
- Recommended Next Step
- Deal Status
- Memo Link
- CIM Document Link
- Date Processed
- Analyst Owner
- Reviewer Notes

Linked records in production:

- CIM Documents
- Financial Metrics
- Risks
- Diligence Questions
- Workflow Runs
- Investment Criteria
- Review Notes

#### CIM Documents

Tracks uploaded source documents and extraction status.

Fields:

- Document Name
- Deal
- Google Drive File Link
- File Upload Time
- Extraction Status
- Extraction Tool
- Raw Text Available
- Extraction Error
- Page Count
- Date Processed

#### Financial Metrics

Stores extracted financial values for the linked deal.

Fields:

- Metric ID
- Deal
- Period
- Revenue
- Revenue Growth
- Gross Margin
- EBITDA
- EBITDA Margin
- Capex
- Net Working Capital
- Free Cash Flow
- Notes

#### Risks

Stores AI-flagged risk items for human review.

Fields:

- Risk ID
- Deal
- Risk Category
- Risk Description
- Severity
- Evidence / Rationale
- Reviewer Status
- Owner
- Follow-Up Needed

#### Diligence Questions

Tracks generated diligence questions and follow-up ownership.

Fields:

- Question ID
- Deal
- Question
- Category
- Priority
- Owner
- Status
- Due Date
- Source / Rationale

#### Workflow Runs

Measures automation performance and project impact.

Fields:

- Run ID
- Deal
- CIM Document
- Upload Time
- Processing Completed Time
- Processing Duration Minutes
- Extraction Status
- OpenAI Status
- Airtable Write Status
- Memo Generation Status
- Slack Notification Status
- Fields Extracted Count
- Missing Fields Count
- Risks Created Count
- Diligence Questions Created Count
- Estimated Manual Minutes Saved
- Error Message

#### Investment Criteria

Stores explainable scoring dimensions tied to a deal.

Fields:

- Criterion
- Deal
- Description
- Scoring Notes
- Target / Threshold
- Weight
- Score

#### Review Notes

Captures human-in-the-loop commentary.

Fields:

- Deal
- Reviewer
- Review Stage
- Decision
- Main Concern
- Follow-Up Request
- Notes
- Review Date

## Airtable Interfaces

### Executive Dashboard

Purpose:

Give an investment team a portfolio-level view of processed CIMs, fit scores, pipeline recommendations, and workflow health.

Live components:

- KPI cards for total deals, average fit score, average data completeness, and open diligence questions
- Recommendation pipeline chart
- Deal prioritization matrix using fit score vs data completeness
- Deal review table with revenue, EBITDA, status, next step, and deadlines
- Workflow Health table from Workflow Runs

### Deal Review

Purpose:

Support single-deal review for analyst and IC prep.

Live components:

- Deal Summary
- Financial Metrics
- Investment Criteria
- Risks
- Diligence Questions
- Workflow Runs

### Operational Views

Key live views:

- Needs Diligence Questions
- Needs Investment Criteria

These views self-clear after downstream automation creates the linked records.

## Slack Alert Design

Live Slack output posts to the DealLens alerts channel with:

```text
DealLens Alert: New CIM Processed

Company: {Company Name}
Sector: {Sector} / {Subsector}
Revenue: {Revenue}
EBITDA: {EBITDA}
Fit Score: {Fit Score}
Data Completeness: {Data Completeness}
Recommended Next Step: {Recommended Next Step}
Deal Status: {Deal Status}
Risks Flagged: {Risks Created Count}

Source Document:
{Google Drive URL}
```

## Google Docs Memo Design

Live memo output creates a first-pass IC memo with:

- executive summary
- transaction overview
- key screening metrics
- business overview
- investment highlights
- growth thesis
- key risks
- preliminary diligence priorities
- source materials
- internal-use disclaimer

Memo links are written back to `Deals.Memo Link`.

## OpenAI Output Contract

OpenAI returns structured JSON matching the project schema.

Required top-level keys:

```json
{
  "deal": {},
  "financial_metrics": [],
  "risks": [],
  "diligence_questions": [],
  "scoring": {},
  "memo": {},
  "missing_fields": [],
  "recommended_next_step": "",
  "workflow_metrics": {}
}
```

## Build Phases

### Phase 0 - Project Setup and Scope Lock

Status: completed

### Phase 1 - Data Model and Airtable Base

Status: completed

### Phase 2 - Sample CIM Dataset

Status: completed

### Phase 3 - Prompting and Structured Extraction

Status: completed

### Phase 4 - Zapier Orchestration MVP

Status: completed

Deliverables achieved:

- working three-Zap automation architecture
- linked Airtable records generated from uploaded CIMs
- Slack alerts
- Google Docs memo generation
- workflow run logging

### Phase 5 - Memo Generation and Slack Alerts

Status: completed

Deliverables achieved:

- live Google Docs memo template
- memo generation in Zap 1
- memo link write-back to Deals
- live Slack alert formatting in Zap 1

### Phase 6 - Airtable Interfaces and Dashboards

Status: completed

Deliverables achieved:

- Executive Dashboard
- Deal Review interface
- dashboard metrics tied to live workflow data

### Phase 7 - Measurement and Impact Story

Status: in_progress

Current tracked signals:

- Fields Extracted Count
- Missing Fields Count
- Risks Created Count
- Diligence Questions Created Count
- Estimated Manual Minutes Saved
- workflow success states across extraction, OpenAI, Airtable, memo, and Slack

### Phase 8 - QA, Edge Cases, and Hardening

Status: completed

Acceptance achieved:

- three sample CIMs run end to end
- failures surfaced and debugged during build
- generalized output across Northstar, MedAxis, and BrightCart
- no hardcoded-company leakage in final workflow state

### Phase 9 - Portfolio Packaging

Status: in_progress

Remaining work:

- refresh README and docs
- finalize recruiter-facing case study
- finalize demo script and screenshots

## Tracking Rules for Codex

When working on this project:

- Treat CODEX.md as the source of truth.
- Update phase statuses as work progresses.
- After each completed phase, output a PowerShell git commit line for the user to copy and paste.
- Use one of these statuses: pending, in_progress, completed, blocked.
- Keep changes scoped to the active phase unless the user asks otherwise.
- Record major architecture decisions in the Decision Log.
- Record unresolved issues in the Open Questions section.
- Do not introduce tools outside the locked stack without user approval.
- Do not use real confidential CIMs or sensitive personal/company data.
- Prefer concrete artifacts over abstract planning.
- Validate outputs with sample data before marking a phase completed.

## Decision Log

| Date | Decision |
|---|---|
| 2026-04-21 | Project will focus on CIM-to-investment-memo automation for private equity. |
| 2026-04-21 | Zapier and Airtable are locked as core tools. |
| 2026-04-21 | Slack will be used for analyst alerts because the user already has Slack/API set up. |
| 2026-04-21 | Supabase will not be used because the user's free-tier projects are already occupied. |
| 2026-04-21 | Looker Studio will not be used; Airtable interfaces will handle dashboarding. |
| 2026-04-21 | Airtable will be used as an application layer, not just a data store. |
| 2026-04-21 | Project name selected: DealLens. |
| 2026-04-21 | PDF.co selected as the default PDF text extraction provider for the MVP. |
| 2026-04-21 | Local secrets will live in .env, with .env.example committed as the template. |
| 2026-04-21 | Airtable setup restarted from a clean blank base using CSV imports because the AI-generated base created dependencies and duplicate fields. |
| 2026-04-21 | Final sample set locked to three synthetic CIMs: Northstar, MedAxis, BrightCart. |
| 2026-04-22 | Added JSON schema output contract for Zapier structured output via GitHub raw URL. |
| 2026-04-27 | Confirmed single-loop-per-Zap limitation; split downstream automations into multiple Zaps. |
| 2026-04-29 | Finalized three-Zap architecture: CIM Intake, Diligence Builder, Investment Criteria Builder. |
| 2026-05-01 | Airtable interfaces completed with Executive Dashboard and Deal Review pages. |
| 2026-05-02 | Added Slack alert formatting, Google Docs memo generation, and memo link write-back to Deals. |

## Open Questions

- Should BrightCart and MedAxis be re-run periodically to demonstrate repeatability on fresh documents?
- Should Review Notes become a fully active analyst-collaboration layer in a future phase?
- Should the next enhancement be failure alerts, memo packet export, or Slack message enrichment?

## Non-Goals

- Do not automate live investment decisions.
- Do not use confidential or proprietary CIMs.
- Do not represent AI outputs as investment advice.
- Do not build a production-grade deal CRM.
- Do not add Supabase or Looker Studio.
- Do not depend on paid Airtable extensions for dashboarding.

## Future Enhancements

- Add failure-path Slack alerts.
- Add duplicate company detection.
- Add exportable IC packet bundling memo plus linked deal artifacts.
- Add review-note collaboration workflow.
- Add benchmark comparison against public comps.
- Add multi-CIM comparison view.
- Add field-level confidence scores and source citations.
