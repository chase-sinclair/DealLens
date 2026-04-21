# OpenAI Extraction Prompt

Status: draft placeholder

Goal:

Convert extracted CIM text into structured JSON matching the DealLens output contract in `CODEX.md`.

Requirements:

- Return valid JSON only.
- Use `not_disclosed` when a field is unavailable.
- Do not fabricate financial values.
- Identify missing critical fields.
- Extract deal fields, financial metrics, risks, diligence questions, scoring, memo sections, and recommended next step.

Prompt will be drafted in Phase 3.
