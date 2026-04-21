# DealLens Setup

This file tracks the local configuration needed to build and demo DealLens.

## 1. Environment File

Create a local `.env` from the template:

```text
.env.example -> .env
```

Fill only the values needed for the current phase. Do not commit `.env`.

Current local config status:

```text
Airtable token and base ID: configured
OpenAI API key: configured
PDF.co API key: configured
Slack webhook and channel ID: configured
Google Drive folder IDs: configured
Google Docs memo template ID: configured
Zapier app connections: pending
```

## 2. Required Accounts And Connections

| Tool | Required Setup | Notes |
|---|---|---|
| Google Drive | Intake folder and archive folder | Folder IDs go in `.env` once created. |
| Zapier | Connected apps | Connect Google Drive, PDF.co, OpenAI, Airtable, Google Docs, Slack. |
| PDF.co | API key | Default extraction provider for MVP. |
| OpenAI | API key | Used for structured CIM extraction and memo drafting. |
| Airtable | Personal access token and base ID | Use Free tier; Airtable is the deal operating system. |
| Google Docs | Memo template document | Template ID goes in `.env` once created. |
| Slack | Channel and alert configuration | User already has Slack/API setup. Confirm channel. |

## 3. Recommended Folder Names

Google Drive:

```text
DealLens/
  CIM Intake/
  CIM Archive/
  Generated Memos/
```

## 4. Airtable Base

Base name:

```text
PE CIM Intelligence Pipeline
```

Use `airtable/schema.md` and `CODEX.md` for the full schema.

## 5. Zapier MVP

Initial Zap:

```text
New Google Drive file
-> PDF.co text extraction
-> OpenAI structured extraction
-> Airtable record creation
-> Google Docs memo generation
-> Slack alert
```

## 6. Secrets Handling

- Keep `.env` local.
- Keep real API keys out of docs, screenshots, and portfolio artifacts.
- Use synthetic CIMs only.
- Scrub screenshots before publishing.
