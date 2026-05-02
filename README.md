# DealLens

DealLens is a portfolio-ready private equity CIM intelligence workflow that turns uploaded CIM PDFs into structured deal records, linked financial metrics, risk flags, diligence questions, workflow run logs, Slack alerts, Google Docs IC memos, and Airtable review interfaces.

It was built to demonstrate practical AI workflow design for financial services: a real manual process, a multi-step automation architecture, measurable operational impact, and a polished review experience for analysts and investment teams.

## What It Does

When a CIM lands in a Google Drive intake folder, DealLens automatically:

- extracts PDF text with PDF.co
- structures the deal with OpenAI
- creates linked Airtable records across the operating base
- scores the opportunity for first-pass PE review
- generates risks and diligence questions
- logs workflow activity and estimated time saved
- posts a Slack alert for the analyst team
- generates a first-pass IC memo in Google Docs
- writes the memo link back to Airtable

## Live MVP Architecture

### Zap 1 - CIM Intake

Google Drive upload trigger that:

1. detects a new PDF in `CIM Intake`
2. extracts document text with PDF.co
3. sends text to OpenAI for structured JSON extraction
4. normalizes metrics for Airtable field types
5. creates Airtable records for:
   - Deals
   - CIM Documents
   - Financial Metrics
   - Workflow Runs
6. posts a Slack alert to the DealLens alert channel
7. creates a Google Docs first-pass IC memo
8. updates the Deal with the memo link
9. loops through and creates linked Risk records

### Zap 2 - Diligence Builder

Airtable-triggered workflow that:

1. watches the `Needs Diligence Questions` Deals view
2. generates diligence questions from structured deal data with OpenAI
3. creates a Workflow Runs record for the diligence run
4. loops through and creates linked Diligence Question records

### Zap 3 - Investment Criteria Builder

Airtable-triggered workflow that:

1. watches the `Needs Investment Criteria` Deals view
2. derives scoring dimensions from existing deal fields with Code by Zapier
3. loops through and creates linked Investment Criteria records

## Stack

| Tool | Role |
|---|---|
| Google Drive | CIM intake, archive, and memo storage |
| Zapier | Multi-Zap orchestration layer |
| PDF.co | PDF text extraction |
| OpenAI API | Structured extraction, scoring, memo drafting, diligence generation |
| Airtable | Deal operating system, dashboards, workflow tracking, and review interfaces |
| Google Docs | First-pass IC memo generation |
| Slack | Analyst alerts and workflow visibility |

## Airtable Product Surface

### Populated Tables

- `Deals`
- `CIM Documents`
- `Financial Metrics`
- `Risks`
- `Diligence Questions`
- `Workflow Runs`
- `Investment Criteria`

### Interfaces

- `Executive Dashboard`
- `Deal Review`

These surfaces make the product feel like a real PE review workspace instead of a raw automation backend.

## Validated Dataset

The MVP has been tested end to end using three synthetic but realistic CIMs:

- `Northstar Field Services` - proceed to initial review
- `MedAxis Revenue Solutions` - request more information
- `BrightCart Consumer Goods` - pass

The final workflow generalized successfully across all three without hardcoded-company leakage.

## Repository Structure

```text
airtable/      Airtable schema notes, field maps, interface references
docs/          Setup guide, demo story, implementation notes
memos/         Memo template notes and generated memo references
portfolio/     Case study material, screenshots, demo script
prompts/       JSON schema, extraction/scoring/memo prompt assets
qa/            QA checklist and edge-case notes
samples/       Synthetic CIM sources, PDFs, expected outputs
slack/         Slack alert templates
zapier/        Zap architecture notes and field mapping references
```

## Build Source Of Truth

The build plan and implementation history live in:

[CODEX.md](./CODEX.md)

## Current State

DealLens is now a functioning MVP with:

- successful three-CIM end-to-end validation
- working Slack alerts
- working Google Docs memo generation
- memo link write-back to Airtable
- linked review data across the base
- demo-ready Airtable dashboard and deal review interface

## Non-Goals

- Do not use real confidential CIMs.
- Do not automate live investment decisions.
- Do not represent AI outputs as investment advice.
- Do not build a production-grade CRM.
- Do not depend on Supabase, Looker Studio, or paid Airtable extensions.
