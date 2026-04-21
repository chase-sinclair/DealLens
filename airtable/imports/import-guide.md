# Airtable CSV Import Guide

Use this guide to replace the AI-generated Airtable base with a clean CSV-imported base.

## Why We Are Rebuilding

The Airtable AI builder created sample records, generated interfaces, automations, duplicate fields, and dependencies. That made schema cleanup slower than starting fresh.

The clean approach:

```text
Blank Airtable base -> CSV imports -> field type cleanup -> linked records -> interfaces later
```

## Step 1 - Create A New Blank Base

In Airtable:

1. Go to the workspace home.
2. Create a new base.
3. Choose blank/base from scratch, not AI builder.
4. Name it:

```text
PE CIM Intelligence Pipeline
```

If Airtable requires a first table, name it:

```text
Deals
```

## Step 2 - Import Header-Only CSVs

Import these header-only CSVs as separate tables. They are intentionally empty except for field names so Airtable creates the schema without importing sample records.

1. `deals.csv` -> `Deals`
2. `cim_documents.csv` -> `CIM Documents`
3. `financial_metrics.csv` -> `Financial Metrics`
4. `risks.csv` -> `Risks`
5. `diligence_questions.csv` -> `Diligence Questions`
6. `workflow_runs.csv` -> `Workflow Runs`
7. `investment_criteria.csv` -> `Investment Criteria`
8. `review_notes.csv` -> `Review Notes`

Suggested path:

```text
Airtable table menu -> Import data -> CSV file
```

## Step 3 - Fix Key Field Types

After import, Airtable may infer some fields as text. Use `field-types.md` as the checklist.

If Airtable refuses a header-only CSV, add one temporary blank row during import or create the table manually from the header row. Do not use real or confidential CIM data.

Do the most important fields first:

- Currency fields
- Percent fields
- Date fields
- URL fields
- Single select fields
- Linked record fields

## Step 4 - Create Linked Record Fields

CSV import creates text fields for values like `Deal`. Convert or recreate these as linked record fields:

Important Airtable rule:

```text
The primary field cannot be a linked record field.
```

Use normal text primary fields for child tables, then create a separate linked `Deal` field.

| Table | Field | Link Target |
|---|---|---|
| CIM Documents | Deal | Deals |
| Financial Metrics | Deal | Deals |
| Risks | Deal | Deals |
| Diligence Questions | Deal | Deals |
| Workflow Runs | Deal | Deals |
| Workflow Runs | CIM Document | CIM Documents |
| Review Notes | Deal | Deals |

If conversion is awkward, create a new linked field named `Deal Link`, link records, then hide the original text field.

Primary fields by table:

| Table | Primary Field |
|---|---|
| Deals | Company Name |
| CIM Documents | Document Name |
| Financial Metrics | Metric ID |
| Risks | Risk ID |
| Diligence Questions | Question ID |
| Workflow Runs | Run ID |
| Investment Criteria | Criterion |
| Review Notes | Review Note ID |

## Step 5 - Keep Interfaces For Later

Do not build interfaces until tables and field types are stable.

Phase 6 will build:

- Analyst Review Queue
- Deal Detail Page
- Executive Deal Dashboard
- Workflow Impact Dashboard
- Diligence Tracker

## Step 6 - Update .env

The new clean base has a new base ID. Copy the new base ID from the Airtable URL:

```text
https://airtable.com/appXXXXXXXXXXXXXX/...
```

Update local `.env`:

```text
AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
```

Do not paste the personal access token or `.env` values into chat.
