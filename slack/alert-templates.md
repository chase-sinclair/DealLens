# Slack Alert Templates

## Successful CIM Processing

```text
New CIM processed: {Company Name}

Fit Score: {Fit Score}/100
Sector: {Sector}
Revenue: {Revenue}
EBITDA: {EBITDA}
EBITDA Margin: {EBITDA Margin}

Top Risk: {Top Risk}
Missing Fields: {Missing Fields}
Recommended Next Step: {Recommended Next Step}

Airtable Review: {Airtable URL}
Memo Draft: {Google Docs URL}
CIM Source: {Google Drive URL}
```

## Missing Critical Fields

```text
DealLens needs analyst review: {Company Name}

Critical missing fields: {Missing Fields}
Recommended action: request supplemental information before first-pass memo review.

Airtable Review: {Airtable URL}
CIM Source: {Google Drive URL}
```

## Processing Failure

```text
DealLens processing failed: {Document Name}

Failure step: {Failure Step}
Error: {Error Message}

Workflow Run: {Airtable Workflow Run URL}
CIM Source: {Google Drive URL}
```
