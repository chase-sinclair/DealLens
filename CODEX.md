# DealLens - Build Playbook

## Project Name

DealLens

Full project title:

```text
DealLens: CIM Intelligence Pipeline for Private Equity
```

## Project Goal

Build a portfolio-ready private equity automation project that identifies a manual business process, designs an automated solution, and measures the operational impact.

DealLens automates first-pass CIM review. A CIM PDF is uploaded to Google Drive, processed through Zapier, converted into structured deal intelligence with AI, stored and reviewed in Airtable, drafted into a Google Docs investment memo, and announced in Slack for analyst review.

## Positioning

Recruiter-facing summary:

> Built a Zapier-orchestrated CIM review pipeline using OpenAI for document intelligence, Airtable as a PE deal operating system, Google Docs for memo generation, and Slack for analyst review alerts. The workflow converts unstructured CIM PDFs into structured deal records, memo drafts, diligence questions, risk flags, and dashboards measuring processing time, field completeness, and estimated analyst hours saved.

## Locked Stack

| Tool | Role |
|---|---|
| Google Drive | CIM intake folder and document archive |
| Zapier | Main automation orchestrator |
| PDF.co or Docparser | PDF text extraction |
| OpenAI API | Structured extraction, scoring, risks, diligence questions, memo drafting |
| Airtable | Deal operating system, review workspace, dashboards, forms, workflow metrics |
| Google Docs | First-pass investment memo output |
| Slack | Analyst alerts, missing-field notices, workflow summaries |

Do not use Supabase or Looker Studio for this build.

## Core Workflow

1. User uploads a CIM PDF to a Google Drive intake folder.
2. Zapier detects the new file.
3. PDF.co extracts the raw text. Docparser is reserved as a fallback if PDF.co is insufficient.
4. OpenAI converts the extracted text into structured deal intelligence.
5. Zapier creates or updates Airtable records.
6. Zapier creates a Google Docs first-pass memo.
7. Zapier posts a Slack alert with review links and key deal context.
8. Airtable interfaces update automatically for analyst review, diligence tracking, and workflow impact measurement.

## Airtable Application Design

### Base

Base name:

```text
PE CIM Intelligence Pipeline
```

### Tables

#### Deals

Primary table for one record per target company or CIM.

Fields:

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
- Missing Fields
- Fit Score
- Data Completeness Score
- Recommended Next Step
- Deal Status
- Memo Link
- CIM Document Link
- Date Processed
- Analyst Owner
- Reviewer Notes

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

Stores extracted or calculated financial values.

Fields:

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

- Deal
- Risk Category
- Risk Description
- Severity
- Evidence / Rationale
- Reviewer Status
- Owner
- Follow-Up Needed

Risk categories:

- Financial Quality
- Customer Concentration
- Market
- Competitive Position
- Management
- Operations
- Legal / Regulatory
- Data Missing

#### Diligence Questions

Tracks generated diligence questions and follow-up ownership.

Fields:

- Deal
- Question
- Category
- Priority
- Owner
- Status
- Due Date
- Source / Rationale

Question categories:

- Financial
- Commercial
- Customer
- Market
- Operations
- Management
- Legal
- Technology
- Tax

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

Stores the target PE thesis and scoring thresholds.

Fields:

- Criterion
- Description
- Weight
- Target / Threshold
- Scoring Notes

Default thesis:

- B2B services or niche software-enabled services
- Revenue between $10M and $100M
- EBITDA margin greater than 10%
- Recurring or repeat revenue
- Fragmented market
- Low customer concentration
- US-based
- Founder-owned or family-owned preferred
- Clear add-on or value creation opportunity

#### Review Notes

Captures human-in-the-loop feedback.

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

Build these interfaces inside Airtable Free.

### Analyst Review Queue

Purpose:

Give an analyst one place to triage newly processed CIMs.

Components:

- List of deals with Deal Status = New or Needs Analyst Review
- Fit Score
- Sector
- Revenue
- EBITDA
- Missing Fields
- Top Risk
- Recommended Next Step
- Link to memo
- Status update controls

### Deal Detail Page

Purpose:

Support full human review for a single target company.

Components:

- Company overview
- Transaction summary
- Financial snapshot
- Investment highlights
- Growth opportunities
- Key risks
- Diligence questions
- Reviewer notes
- Memo and CIM document links

### Executive Deal Dashboard

Purpose:

Show pipeline-level deal intelligence.

Components:

- Deals processed
- Deals by status
- Deals by sector
- Average Fit Score
- High-fit deals
- Pass / proceed distribution
- Upcoming process deadlines

### Workflow Impact Dashboard

Purpose:

Prove measurable process improvement.

Components:

- Average processing duration
- Estimated manual time saved
- Total estimated hours saved
- Average missing fields per CIM
- Extraction success rate
- Memo generation success rate
- Slack notification success rate

### Diligence Tracker

Purpose:

Track generated diligence work as owned action items.

Components:

- Open diligence questions
- High-priority questions
- Questions by category
- Questions by owner
- Overdue questions
- Questions tied to high-severity risks

## Forms

### Manual Deal Intake Form

Use when a deal is submitted without the Google Drive CIM upload flow.

Fields:

- Company Name
- Sector
- Source
- Banker / Advisor
- Revenue Range
- EBITDA Range
- CIM Attachment
- Initial Notes
- Process Deadline

### Reviewer Feedback Form

Use to capture mock VP, principal, or partner feedback.

Fields:

- Deal
- Decision
- Main Concern
- Follow-Up Request
- Proceed / Pass / More Info Needed
- Notes

## Slack Alert Design

Post to the configured Slack channel when a CIM is processed.

Message template:

```text
New CIM processed: {Company Name}

Fit Score: {Fit Score}/100
Sector: {Sector}
Revenue: {Revenue}
EBITDA: {EBITDA}
EBITDA Margin: {EBITDA Margin}

Top Risk: {Top Risk}
Missing Fields: {Missing Fields}
Recommended Next Step: {Recommended Next Step}

Airtable Review: {Airtable URL}
Memo Draft: {Google Docs URL}
CIM Source: {Google Drive URL}
```

Post a separate alert when extraction fails or when critical fields are missing.

## OpenAI Output Contract

OpenAI must return structured JSON. Do not depend on prose parsing.

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
  "recommended_next_step": ""
}
```

Deal object fields:

- company_name
- sector
- subsector
- headquarters
- founded_year
- ownership_seller_type
- revenue
- revenue_growth
- ebitda
- ebitda_margin
- business_model
- revenue_model
- customer_segments
- customer_concentration
- geographic_footprint
- employee_count
- transaction_type
- banker_advisor
- process_deadline
- investment_highlights
- growth_opportunities
- key_risks_summary

Scoring object fields:

- revenue_fit
- margin_fit
- business_model_fit
- market_fragmentation
- customer_concentration_risk
- growth_opportunity
- data_completeness
- overall_fit_score
- scoring_rationale

Memo object sections:

- company_overview
- transaction_summary
- business_model
- market_industry_context
- financial_snapshot
- investment_highlights
- growth_thesis
- key_risks
- preliminary_diligence_questions
- initial_recommendation

## Build Phases

### Phase 0 - Project Setup and Scope Lock

Status: in_progress

Objective:

Confirm the project boundaries, stack, mock data strategy, and demo success criteria.

Tasks:

- Create or update this CODEX.md file as the source of truth.
- Create .env.example and .gitignore.
- Keep real secrets in a local .env file only.
- Create docs/setup.md for configuration and access notes.
- Confirm Google Drive, Zapier, Airtable, OpenAI, Google Docs, and Slack access.
- Use PDF.co as the default PDF text extraction provider for the MVP.
- Decide whether CIMs will be synthetic PDFs, public investor presentations, or both.
- Define the demo story and sample deal thesis.
- Create a lightweight repository structure for prompts, sample data, docs, and implementation notes.

Deliverables:

- CODEX.md
- .env.example
- .gitignore
- docs/setup.md
- Project folder structure
- Tool access checklist
- Initial PE investment criteria

Acceptance criteria:

- All locked tools are named and assigned a role.
- Non-goals are explicit: no Supabase, no Looker Studio, no real confidential CIMs.
- The user can explain the project in one recruiter-facing paragraph.

### Phase 1 - Data Model and Airtable Base

Status: completed

Objective:

Build the Airtable base as a real PE deal operating system.

Tasks:

- Create Airtable base: PE CIM Intelligence Pipeline.
- Use a blank Airtable base plus CSV imports instead of the Airtable AI-generated base.
- Create all core tables.
- Add fields with correct data types.
- Configure linked records between Deals, CIM Documents, Financial Metrics, Risks, Diligence Questions, Workflow Runs, and Review Notes.
- Create views for analyst review, high-fit deals, missing fields, extraction failures, open diligence questions, and workflow metrics.
- Add initial Investment Criteria records.

Deliverables:

- Airtable base
- Tables, fields, relationships, and views
- Initial investment thesis scoring criteria

Acceptance criteria:

- A manually entered deal can link to documents, risks, diligence questions, workflow runs, and review notes.
- Views support the analyst workflow without requiring raw table browsing.
- Airtable remains within Free-tier constraints.

### Phase 2 - Sample CIM Dataset

Status: completed

Objective:

Create realistic, non-confidential CIM inputs for the demo.

Tasks:

- Create 3-5 synthetic CIMs representing strong, medium, and poor-fit deals.
- Include variation in sector, revenue, EBITDA margin, customer concentration, growth rate, and missing data.
- Store sample CIM PDFs in Google Drive intake/archive folders.
- Create expected output notes for each CIM to support accuracy checks.

Deliverables:

- Synthetic CIM PDFs
- Expected extraction benchmark document
- Google Drive folder structure

Acceptance criteria:

- At least one CIM should be a strong fit.
- At least one CIM should have missing critical fields.
- At least one CIM should produce clear pass or request-more-info recommendation.
- No confidential or private third-party data is used.

### Phase 3 - Prompting and Structured Extraction

Status: pending

Objective:

Build reliable OpenAI prompts that convert CIM text into structured JSON.

Tasks:

- Draft the extraction prompt.
- Draft the scoring prompt or combine scoring into the extraction prompt.
- Draft the memo generation prompt.
- Require valid JSON output matching the output contract.
- Include missing-field detection.
- Include risk categorization.
- Include diligence question generation.
- Test prompts against all sample CIMs.
- Record prompt versions and observed failures.

Deliverables:

- Extraction prompt
- Memo prompt
- Scoring logic
- JSON schema or output contract documentation
- Prompt test notes

Acceptance criteria:

- Outputs can be mapped to Airtable fields without manual rewriting.
- Missing critical fields are explicitly listed.
- Risks and diligence questions are specific to the deal.
- Overall fit score includes rationale.

### Phase 4 - Zapier Orchestration MVP

Status: pending

Objective:

Create the first working automation from CIM upload to Airtable record creation.

Tasks:

- Create Google Drive trigger for new CIM upload.
- Connect PDF.co or Docparser text extraction.
- Send extracted text to OpenAI.
- Parse structured JSON output in Zapier.
- Create Deal record in Airtable.
- Create linked CIM Document record.
- Create linked Risk records.
- Create linked Diligence Question records.
- Create Workflow Run record.
- Add basic error handling paths for extraction or AI failures.

Deliverables:

- Working Zapier MVP
- Airtable records generated from one uploaded CIM
- Workflow run logging

Acceptance criteria:

- Uploading a sample CIM creates a complete Airtable deal package.
- Deal, document, risks, diligence questions, and workflow run records are linked correctly.
- Failed extraction creates a visible failure state instead of silently stopping.

### Phase 5 - Memo Generation and Slack Alerts

Status: pending

Objective:

Add business-facing outputs: first-pass memo and analyst notification.

Tasks:

- Create Google Docs memo template.
- Map OpenAI memo sections into the Google Docs template.
- Store generated memo link on the Airtable Deal record.
- Configure Slack alert for successful CIM processing.
- Configure Slack alert for missing critical fields or processing failures.
- Include Airtable review link, memo link, and CIM source link in Slack messages.

Deliverables:

- Google Docs memo template
- Generated memo drafts
- Slack alert templates
- Working Slack notifications

Acceptance criteria:

- Each processed CIM generates a readable first-pass memo.
- Slack alert gives enough context for an analyst to decide what to review next.
- Missing-field alerts are clear and actionable.

### Phase 6 - Airtable Interfaces and Dashboards

Status: pending

Objective:

Turn Airtable into a polished review application and impact dashboard.

Tasks:

- Build Analyst Review Queue interface.
- Build Deal Detail Page interface.
- Build Executive Deal Dashboard interface.
- Build Workflow Impact Dashboard interface.
- Build Diligence Tracker interface.
- Validate dashboard metrics against Workflow Runs records.
- Ensure interface pages are navigable and presentation-ready.

Deliverables:

- Airtable review app
- Airtable dashboards
- Demo-ready interface flow

Acceptance criteria:

- A reviewer can process a deal from queue to decision inside Airtable.
- Dashboards show deal pipeline, workflow impact, and diligence workload.
- Dashboarding uses Airtable interfaces, not paid extensions.

### Phase 7 - Measurement and Impact Story

Status: pending

Objective:

Quantify before/after process improvement.

Tasks:

- Define manual baseline assumptions.
- Time one manual first-pass CIM review for comparison.
- Time automated processing and review.
- Calculate estimated minutes saved per CIM.
- Track extraction completeness.
- Track memo generation success.
- Track missing field rates.
- Create summary metrics in Airtable.

Deliverables:

- Before/after impact table
- Airtable metrics
- Recruiter-ready project narrative

Acceptance criteria:

- Impact story includes time saved, consistency gains, and workflow visibility.
- Metrics are grounded in tracked Workflow Runs, not only estimates.
- Any assumptions are documented clearly.

### Phase 8 - QA, Edge Cases, and Hardening

Status: pending

Objective:

Make the demo reliable enough to show confidently.

Tasks:

- Test all sample CIMs end to end.
- Test missing-field CIM.
- Test extraction failure handling.
- Test duplicate upload handling.
- Test Slack alerts.
- Test memo link creation.
- Review Airtable field mappings.
- Review prompt outputs for hallucinated data.
- Add explicit "not disclosed" handling where CIM data is unavailable.

Deliverables:

- QA checklist
- Known limitations list
- Fixed Zapier/Airtable mapping issues

Acceptance criteria:

- At least 3 sample CIMs run end to end.
- Failures are visible and understandable.
- The workflow does not fabricate undisclosed financial values.
- Demo path is stable.

### Phase 9 - Portfolio Packaging

Status: pending

Objective:

Package the project so it can be shared with recruiters and discussed in interviews.

Tasks:

- Write README or case study.
- Include problem, manual workflow, automated design, architecture, data model, screenshots, metrics, and lessons learned.
- Create simple architecture diagram.
- Capture screenshots of Airtable interfaces, Slack alert, memo output, and Zapier flow.
- Record a short demo script.
- Add a limitations and future improvements section.

Deliverables:

- Portfolio case study
- Demo script
- Architecture diagram
- Screenshots

Acceptance criteria:

- A recruiter can understand the business value in under 60 seconds.
- A technical reviewer can understand the architecture and data model.
- The project demonstrates automation, AI extraction, PE workflow knowledge, Airtable app design, Slack integration, and measurable impact.

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
| 2026-04-21 | PDF.co selected as the default PDF text extraction provider for the MVP; Docparser remains a fallback. |
| 2026-04-21 | Local secrets will live in .env, with .env.example committed as the template. |
| 2026-04-21 | Airtable, OpenAI, PDF.co, Slack, Google Drive, and Google Docs config values were added locally to .env by the user. |
| 2026-04-21 | Airtable setup will restart from a clean blank base using CSV imports because the AI-generated base created dependencies and duplicate fields. |
| 2026-04-21 | Airtable import CSVs were changed to header-only files after Airtable reported invalid sample data during import. |
| 2026-04-21 | Clean Airtable schema was created with proper primary fields and linked Deal relationships on child tables. |
| 2026-04-21 | Phase 2 synthetic CIM dataset completed with three markdown source CIMs, generated PDFs, and expected extraction benchmarks. |
| 2026-04-21 | User-supplied designed Northstar PDF replaced the generated Northstar PDF as the workflow input artifact; Markdown remains a clean reference source. |
| 2026-04-21 | User-supplied designed MedAxis PDF replaced the generated MedAxis PDF as the workflow input artifact; extraction verified cleanly without citation artifacts. |
| 2026-04-21 | User-supplied designed BrightCart PDF replaced the generated BrightCart PDF as the workflow input artifact; extraction verified cleanly without citation artifacts. |

## Open Questions

- Should sample CIMs be fully synthetic, public investor presentations, or a mix?
- Which Slack channel should receive demo alerts?
- Should OpenAI calls happen entirely inside Zapier or through a lightweight custom endpoint later?
- What target PE strategy should the demo thesis emphasize: B2B services, vertical SaaS, healthcare services, industrial services, or another sector?

## Non-Goals

- Do not automate live investment decisions.
- Do not use confidential or proprietary CIMs.
- Do not represent AI outputs as investment advice.
- Do not build a production-grade deal CRM.
- Do not add Supabase or Looker Studio.
- Do not depend on paid Airtable extensions for dashboarding.

## Future Enhancements

- Add OCR support for scanned PDFs.
- Add field-level confidence scores.
- Add source citations or page references for extracted claims.
- Add duplicate company detection.
- Add email-based CIM intake in addition to Google Drive.
- Add benchmark comparison against public comps.
- Add multi-CIM comparison view.
- Add exportable investment committee packet.
- Add human approval before Slack distribution.
