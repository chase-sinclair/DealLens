# Tool Access Checklist

Track setup status for the locked DealLens stack.

| Tool | Needed For | Status | Notes |
|---|---|---|---|
| Google Drive | CIM intake folder and document archive | configured | Intake, archive, and generated memo folders created; IDs stored locally in `.env`. |
| Zapier | Workflow orchestration | pending | Connect Google Drive, PDF extraction, OpenAI, Airtable, Google Docs, and Slack. |
| PDF.co | PDF text extraction | configured | API key stored locally in `.env`; default extraction provider for MVP. |
| Docparser | Alternate PDF extraction | not planned | Use only if PDF.co is insufficient. |
| OpenAI API | Structured extraction and memo generation | configured | API key stored locally in `.env`; Zapier connection still needed. |
| Airtable | Deal operating system and dashboards | configured | Base created; personal access token and base ID stored locally in `.env`. |
| Google Docs | Memo generation | configured | First-pass memo template created; template ID stored locally in `.env`. |
| Slack | Analyst alerts | configured | DealLens workspace/webhook/channel created; values stored locally in `.env`. |
