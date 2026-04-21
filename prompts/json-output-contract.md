# DealLens JSON Output Contract

Version: v1

The extraction prompt must return valid JSON with this shape.

```json
{
  "deal": {
    "company_name": "string",
    "sector": "string",
    "subsector": "string",
    "headquarters": "string",
    "founded_year": 0,
    "ownership_seller_type": "string",
    "revenue": 0,
    "revenue_growth": 0,
    "ebitda": 0,
    "ebitda_margin": 0,
    "business_model": "string",
    "revenue_model": "string",
    "customer_segments": "string",
    "customer_concentration": "string",
    "geographic_footprint": "string",
    "employee_count": 0,
    "transaction_type": "string",
    "banker_advisor": "string",
    "process_deadline": "YYYY-MM-DD",
    "investment_highlights": "string",
    "growth_opportunities": "string",
    "key_risks_summary": "string",
    "missing_fields": "string",
    "fit_score": 0,
    "data_completeness_score": 0,
    "recommended_next_step": "string",
    "deal_status": "string",
    "memo_link": "not_disclosed",
    "cim_document_link": "not_disclosed",
    "date_processed": "not_disclosed",
    "analyst_owner": "not_disclosed",
    "reviewer_notes": "not_disclosed"
  },
  "financial_metrics": [
    {
      "period": "string",
      "revenue": 0,
      "revenue_growth": 0,
      "gross_margin": 0,
      "ebitda": 0,
      "ebitda_margin": 0,
      "capex": 0,
      "net_working_capital": 0,
      "free_cash_flow": 0,
      "notes": "string"
    }
  ],
  "risks": [
    {
      "risk_category": "string",
      "risk_description": "string",
      "severity": "Low | Medium | High",
      "evidence_rationale": "string",
      "reviewer_status": "Unreviewed",
      "owner": "not_disclosed",
      "follow_up_needed": true
    }
  ],
  "diligence_questions": [
    {
      "question": "string",
      "category": "string",
      "priority": "Low | Medium | High",
      "owner": "not_disclosed",
      "status": "Open",
      "due_date": "not_disclosed",
      "source_rationale": "string"
    }
  ],
  "scoring": {
    "revenue_fit": 0,
    "margin_fit": 0,
    "business_model_fit": 0,
    "market_fragmentation": 0,
    "customer_concentration_risk": 0,
    "growth_opportunity": 0,
    "data_completeness": 0,
    "overall_fit_score": 0,
    "scoring_rationale": "string"
  },
  "memo": {
    "company_overview": "string",
    "transaction_summary": "string",
    "business_model": "string",
    "market_industry_context": "string",
    "financial_snapshot": "string",
    "investment_highlights": "string",
    "growth_thesis": "string",
    "key_risks": "string",
    "preliminary_diligence_questions": "string",
    "initial_recommendation": "string"
  },
  "missing_fields": ["string"],
  "recommended_next_step": "Proceed to initial review | Request more information | Pass | Hold",
  "workflow_metrics": {
    "fields_extracted_count": 0,
    "missing_fields_count": 0,
    "risks_created_count": 0,
    "diligence_questions_created_count": 0,
    "estimated_manual_minutes_saved": 0
  }
}
```

Use `"not_disclosed"` for unavailable values. Use numeric `0` only when the CIM discloses a true zero.
