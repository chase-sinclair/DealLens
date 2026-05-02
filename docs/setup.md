# DealLens Setup

This file tracks the local configuration needed to build, test, and demo DealLens.

## 1. Environment File

Create a local `.env` from the template:

```text
.env.example -> .env
```

Do not commit `.env`.

Current local config status:

```text
Airtable token and base ID: configured
OpenAI API key: configured
PDF.co API key: configured
Slack app connection and alert channel: configured
Google Drive folder IDs: configured
Google Docs memo template ID: configured
Zapier app connections: configured
```

## 2. Required Accounts And Connections

| Tool | Required Setup | Notes |
|---|---|---|
| Google Drive | Intake folder, archive folder, memo folder | Use `CIM Intake`, `CIM Archive`, and `Generated Memos`. |
| Zapier | Connected apps | Connect Google Drive, PDF.co, OpenAI, Airtable, Google Docs, Slack. |
| PDF.co | API key | Default extraction provider for MVP. |
| OpenAI | API key | Used for extraction, scoring, memo drafting, and diligence generation. |
| Airtable | Personal access token and base access | Base name is `DealLens`. |
| Google Docs | Memo template document | Used by Zap 1 for IC memo generation. |
| Slack | Connected workspace and channel | Use the `deallens-alerts` channel for demo alerts. |

## 3. Recommended Google Drive Folder Structure

```text
DealLens/
  CIM Intake/
  CIM Archive/
  Generated Memos/
```

## 4. Airtable Base

Base name:

```text
DealLens
```

Primary live tables:

- Deals
- CIM Documents
- Financial Metrics
- Risks
- Diligence Questions
- Workflow Runs
- Investment Criteria
- Review Notes

Use `airtable/schema.md` and `CODEX.md` for the full schema.

## 5. Live Zap Architecture

### Zap 1 - CIM Intake

```text
New Google Drive file
-> PDF.co extraction
-> OpenAI structured extraction
-> Code normalization
-> Airtable Deal creation
-> Airtable CIM Document creation
-> Airtable Financial Metrics creation
-> Airtable Workflow Run creation
-> Slack alert
-> Google Docs memo generation
-> Airtable Deal memo link update
-> Risk loop and Airtable Risk creation
```

### Zap 2 - Diligence Builder

```text
Airtable New Record in View (Needs Diligence Questions)
-> OpenAI diligence generation
-> Airtable Workflow Run creation
-> Diligence loop
-> Airtable Diligence Question creation
```

### Zap 3 - Investment Criteria Builder

```text
Airtable New Record in View (Needs Investment Criteria)
-> Code by Zapier criteria derivation
-> Criteria loop
-> Airtable Investment Criteria creation
```

## 6. Airtable Interfaces

Live interfaces:

- Executive Dashboard
- Deal Review

## 7. Validated Test Set

Validated end-to-end against:

- Northstar Field Services
- MedAxis Revenue Solutions
- BrightCart Consumer Goods

## 8. Secrets Handling

- Keep `.env` local.
- Keep real API keys out of docs, screenshots, and portfolio artifacts.
- Use synthetic CIMs only.
- Scrub screenshots before publishing outside trusted contexts.
