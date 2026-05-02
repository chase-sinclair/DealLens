# Zapier Build Notes

## Final Architecture

DealLens uses three Zaps because Zapier supports only one loop per Zap and the product needs multiple independent child-record fan-outs.

### Zap 1 - CIM Intake

Trigger:

- New PDF uploaded to Google Drive `CIM Intake`

Actions:

1. PDF.co -> PDF to Anything Converter
2. Code by Zapier -> flatten extracted text and expose page count
3. OpenAI Conversation -> structured JSON extraction using the shared schema
4. Code by Zapier -> normalize percent and metric values for Airtable
5. Airtable -> Create Deal record
6. Airtable -> Create CIM Documents record
7. Airtable -> Create Financial Metrics record
8. Airtable -> Create Workflow Runs record for intake
9. Slack -> Send Channel Message to `deallens-alerts`
10. Google Docs -> Create Document From Template
11. Airtable -> Update Deal with Memo Link
12. Looping by Zapier -> iterate Risks
13. Airtable -> Create Risk record

### Zap 2 - Diligence Builder

Trigger:

- Airtable `Deals` -> New Record in View `Needs Diligence Questions`

Actions:

1. OpenAI Conversation -> generate diligence question JSON
2. Airtable -> Create Workflow Runs record for diligence generation
3. Looping by Zapier -> iterate Diligence Questions
4. Airtable -> Create Diligence Question record

### Zap 3 - Investment Criteria Builder

Trigger:

- Airtable `Deals` -> New Record in View `Needs Investment Criteria`

Actions:

1. Code by Zapier -> derive investment criteria arrays from deal data
2. Looping by Zapier -> iterate criteria rows
3. Airtable -> Create Investment Criteria record

## Key Design Decisions

- PDF.co is the default extraction provider.
- OpenAI schema mode is used for reliable field mapping.
- Percent normalization happens before Airtable writes to avoid field-type conversion issues.
- Diligence Questions and Investment Criteria were split into separate Zaps because nested loops are not supported.
- Memo creation happens before the risk loop so the memo artifact exists even if later steps fail.
- Workflow Runs is populated by both Zap 1 and Zap 2 to support operational dashboards.

## Slack Alert

Current Slack payload includes:

- company
- sector / subsector
- revenue
- EBITDA
- fit score
- data completeness
- recommended next step
- deal status
- risks flagged
- CIM source link

## Memo Generation

Google Docs memo generation uses a styled IC memo template with placeholders for:

- company_name
- memo_date
- company_overview
- transaction_summary
- transaction_type
- sector_subsector
- ownership_seller_type
- headquarters
- process_deadline
- deal_status
- revenue
- ebitda
- revenue_growth
- ebitda_margin
- fit_score
- data_completeness
- business_model
- market_industry_context
- financial_snapshot
- investment_highlights
- growth_thesis
- key_risks
- preliminary_diligence_questions
- cim_source_link
- airtable_review_link

## Known Build Constraints

- Only one Looping by Zapier step can be used per Zap.
- Airtable schema changes can leave stale hidden field IDs in Zapier steps; removing extra fields fixes most of these cases.
- Google Docs placeholder caching may require reselecting the template document after edits.
- Slack alert formatting is intentionally concise for channel readability.

## Error Paths To Watch

- Google Drive sharing restrictions can block PDF.co downloads.
- Stale Airtable field IDs after field deletion/renaming can break create or update steps.
- Stale Airtable record IDs in Zapier tests can break update-step testing even when live runs work.
- Missing placeholder mappings in the memo template can leave unresolved tokens in generated docs.
