# Zapier Screenshot Notes

Screenshots received for the three DealLens Zaps.

## Files to add

```text
cim-intake-zap.png
diligence-builder-zap.png
investment-criteria-builder-zap.png
```

## Zap 1: CIM Intake

Use `cim-intake-zap.png` as the main Zapier workflow visual.

Visible steps:

1. Google Drive — New File In Folder
2. PDF.co — PDF to Anything Converter
3. Code by Zapier — Run JavaScript
4. ChatGPT / OpenAI — Conversation
5. Code by Zapier — Run JavaScript
6. Airtable — Create Record
7. Airtable — Create Record
8. Airtable — Create Record
9. Airtable — Create Record
10. Slack — Send Channel Message
11. Google Docs — Create Document From Template
12. Airtable — Update Record
13. Looping by Zapier — Create Loop From Line Items
14. Airtable — Create Record

Recommended animation:

- Use the screenshot as the base image.
- Do not show messy Zap run output data.
- Animate a green completion highlight/checkmark moving down the visible steps.
- Group the individual Zapier cards into business-language phases:
  1. CIM detected
  2. Text extracted
  3. Deal intelligence structured
  4. Airtable records created
  5. Analyst alerted
  6. IC memo generated
  7. Memo link written back
  8. Risks created

## Zap 2: Diligence Builder

Use `diligence-builder-zap.png` as a supporting Zap scene or a side card in the orchestration scene.

Visible steps:

1. Airtable — New Record
2. ChatGPT / OpenAI — Conversation
3. Airtable — Create Record
4. Looping by Zapier — Create Loop From Line Items
5. Airtable — Create Record

Recommended animation:

- Show after the main Zap 1 sequence as a secondary automation.
- Animate the cards turning green from top to bottom.
- Label it: `Diligence questions generated from structured deal context`.

## Zap 3: Investment Criteria Builder

Use `investment-criteria-builder-zap.png` as a supporting Zap scene or a side card in the orchestration scene.

Visible steps:

1. Airtable — New Record
2. Code by Zapier — Run JavaScript
3. Looping by Zapier — Create Loop From Line Items
4. Airtable — Create Record

Recommended animation:

- Show after the Diligence Builder or alongside it.
- Animate the cards turning green from top to bottom.
- Label it: `Investment criteria rows created for explainable scoring`.

## Direction for Codex / HyperFrames

For the Zapier section, do not try to recreate messy step-completion output. Use the Zap screenshots as clean proof of the automation architecture and generate an animated overlay that simulates completion.

Each key step should light up green one by one with a checkmark or pulse. Use short business-language labels rather than Zapier configuration details.

The intended viewer takeaway is:

```text
Zapier coordinates the end-to-end workflow while Airtable remains the product workspace.
```
