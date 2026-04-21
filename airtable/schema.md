# Airtable Schema

Use this file as the implementation checklist when creating the Airtable base.

Preferred setup path:

```text
Create a blank Airtable base and import the header-only CSV files in airtable/imports.
```

Do not use the Airtable AI app builder for the production demo base. The AI builder creates sample data, generated dependencies, and duplicate fields that slow down schema cleanup.

Base name:

```text
PE CIM Intelligence Pipeline
```

## Core Tables

- Deals
- CIM Documents
- Financial Metrics
- Risks
- Diligence Questions
- Workflow Runs
- Investment Criteria
- Review Notes

## Required Interfaces

- Analyst Review Queue
- Deal Detail Page
- Executive Deal Dashboard
- Workflow Impact Dashboard
- Diligence Tracker

## Required Forms

- Manual Deal Intake Form
- Reviewer Feedback Form

See `CODEX.md` for field-level detail.

See `airtable/imports/import-guide.md` for the CSV import workflow.
