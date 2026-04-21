# QA Checklist

## End-To-End Tests

- [ ] Strong-fit CIM creates complete Airtable deal package.
- [ ] Medium-fit CIM flags missing data.
- [ ] Poor-fit CIM receives pass or request-more-info recommendation.
- [ ] Risks are linked to the correct deal.
- [ ] Diligence questions are linked to the correct deal.
- [ ] Workflow run captures processing duration and statuses.
- [ ] Google Docs memo link is saved to Airtable.
- [ ] Slack success alert includes review links.
- [ ] Missing-field alert is actionable.
- [ ] Extraction failure is visible in Airtable.

## Data Quality Checks

- [ ] AI uses `not_disclosed` for unavailable data.
- [ ] AI does not fabricate financial values.
- [ ] Fit score has rationale.
- [ ] Memo is readable and PE-specific.
- [ ] Diligence questions are specific to the CIM.
