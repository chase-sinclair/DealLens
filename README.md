# DealLens

DealLens is a portfolio-ready private equity automation project that converts unstructured CIM PDFs into structured deal intelligence, first-pass investment memo drafts, diligence questions, risk flags, Slack alerts, and Airtable review dashboards.

The project is designed to demonstrate practical workflow automation, AI-assisted document extraction, PE process knowledge, Airtable application design, Slack integration, and measurable operational impact.

## Stack

| Tool | Role |
|---|---|
| Google Drive | CIM intake and source document archive |
| Zapier | Automation orchestration |
| PDF.co or Docparser | PDF text extraction |
| OpenAI API | Structured extraction, scoring, risk detection, memo drafting |
| Airtable | Deal operating system, review workspace, dashboards, forms, workflow metrics |
| Google Docs | First-pass memo output |
| Slack | Analyst alerts and workflow notifications |

## Build Source Of Truth

The build plan, phase tracking, decisions, and acceptance criteria live in:

[CODEX.md](./CODEX.md)

## Repository Structure

```text
airtable/      Airtable schema, field maps, interface notes
docs/          Setup notes, access checklist, demo story
memos/         Google Docs memo template notes and generated memo references
portfolio/     Case study, screenshots, demo script
prompts/       OpenAI extraction, scoring, and memo prompts
qa/            QA checklist and edge-case notes
samples/       Synthetic CIM dataset notes and expected outputs
slack/         Slack alert templates
zapier/        Zap build notes and field mappings
```

## Current Build Phase

Phase 0 is in progress: project setup and scope lock.

## Non-Goals

- Do not use real confidential CIMs.
- Do not automate live investment decisions.
- Do not represent AI outputs as investment advice.
- Do not use Supabase or Looker Studio.
- Do not depend on paid Airtable extensions for dashboarding.
