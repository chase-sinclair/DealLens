# Zapier Build Notes

## MVP Zap

Trigger:

- New CIM PDF uploaded to Google Drive intake folder.

Actions:

1. Extract PDF text with PDF.co or Docparser.
2. Send extracted text to OpenAI.
3. Parse structured JSON output.
4. Create Airtable Deal record.
5. Create linked Airtable CIM Document record.
6. Create linked Airtable Risk records.
7. Create linked Airtable Diligence Question records.
8. Create Airtable Workflow Run record.
9. Create Google Docs memo.
10. Post Slack notification.

## Error Paths

- PDF extraction failure
- Invalid OpenAI JSON
- Missing critical fields
- Airtable write failure
- Google Docs generation failure
- Slack notification failure
