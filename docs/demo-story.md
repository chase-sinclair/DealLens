# Demo Story

## One-Minute Pitch

DealLens automates the first-pass CIM screening workflow for private equity teams. When a CIM is uploaded to Google Drive, Zapier extracts the PDF text with PDF.co, OpenAI converts it into structured deal intelligence, Airtable becomes the review workspace, Google Docs generates a first-pass IC memo, and Slack notifies the analyst team with deal quality, recommendation, and workflow context.

## The Problem

Before automation, an analyst manually reads a CIM, copies key company and financial data into a tracker, identifies major risks, drafts a first-pass memo, writes diligence questions, and shares a summary with the team. That process is repetitive, inconsistent, and hard to measure.

## The Product

DealLens turns that workflow into a connected operating system with:

- CIM intake from Google Drive
- AI-assisted extraction and scoring
- structured Airtable deal records
- linked financial metrics, risks, diligence questions, workflow runs, and investment criteria
- Google Docs memo generation
- Slack alerts for analyst review
- Airtable interfaces for both pipeline overview and single-deal review

## Live Workflow

### Zap 1 - CIM Intake

A new CIM triggers:

- PDF extraction
- OpenAI parsing
- Deal creation
- CIM Document creation
- Financial Metrics creation
- Workflow Run logging
- Slack notification
- Google Docs memo generation
- memo link write-back
- Risk record creation

### Zap 2 - Diligence Builder

A new Deal in the `Needs Diligence Questions` view triggers:

- OpenAI diligence question generation
- Workflow Run logging
- Diligence Question creation

### Zap 3 - Investment Criteria Builder

A new Deal in the `Needs Investment Criteria` view triggers:

- criteria derivation from deal data
- linked Investment Criteria creation

## Demo Dataset

Three synthetic CIMs are used to show differentiated outcomes:

- `Northstar Field Services` -> proceed to initial review
- `MedAxis Revenue Solutions` -> request more information
- `BrightCart Consumer Goods` -> pass

## What The Reviewer Sees

### Executive Dashboard

- total deals processed
- average fit score
- average data completeness
- open diligence question count
- recommendation pipeline chart
- fit vs completeness prioritization chart
- compact deal review table
- workflow health table

### Deal Review Page

- deal summary
- linked financial metrics
- linked investment criteria
- linked risks
- linked diligence questions
- linked workflow context

## Measured Impact Signals

Tracked in Workflow Runs:

- Fields Extracted Count
- Missing Fields Count
- Risks Created Count
- Diligence Questions Created Count
- Estimated Manual Minutes Saved
- extraction, OpenAI, Airtable, memo, and Slack success states

## Suggested Demo Walkthrough

1. Show the Google Drive intake folder.
2. Show the Slack alert for a processed CIM.
3. Open the Executive Dashboard and explain the recommendation split.
4. Open a single deal in Deal Review.
5. Show the generated memo link on the Deal.
6. Show linked risks, diligence questions, and investment criteria.
7. Close with Workflow Runs and time saved.

## Why It Matters

DealLens demonstrates applied AI product thinking in a PE workflow:

- real document-to-data automation
- human-readable and dashboardable outputs
- explainable scoring rather than black-box recommendations
- measurable operational value instead of vague AI claims
