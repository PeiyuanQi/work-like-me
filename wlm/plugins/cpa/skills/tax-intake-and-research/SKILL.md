---
name: tax-intake-and-research
description: Use when the user asks tax-related questions, needs CPA-style tax intake, wants help organizing tax documents, asks about filing status, deductions, credits, estimated taxes, business expenses, payroll taxes, sales tax, state or federal tax obligations, audits, notices, amended returns, or tax planning. This skill provides general tax workflow support and research organization, not licensed professional tax advice.
---

# Tax Intake And Research

Version: 1.0.0

Support tax-related work by collecting the right facts, checking the right
sources, and separating general information from filing advice.

## Boundaries

- Do not present yourself as a licensed CPA, enrolled agent, tax attorney, or
  paid preparer.
- Do not give definitive filing positions when facts are incomplete, the rule is
  current-year sensitive, or the consequence is material.
- For audits, legal disputes, penalty exposure, amended returns, multi-state
  nexus, crypto, equity compensation, entity restructuring, foreign reporting,
  estate/gift tax, or large dollar amounts, recommend review by a licensed CPA,
  EA, or tax attorney.
- For current law, forms, thresholds, due dates, and agency procedures, verify
  against official sources before answering.

## Intake

Collect only what is needed for the question:

- Tax year and filing deadline involved
- Country, state, city, and residency or nexus facts
- Individual, household, sole proprietor, partnership, corporation, nonprofit,
  trust, or estate context
- Filing status, dependents, income types, deductions, credits, payments, and
  prior-year carryovers when relevant
- Entity ownership, accounting method, payroll setup, sales channels, and worker
  classification when business tax is involved
- Documents available, such as W-2, 1099, K-1, 1098, brokerage statements,
  payroll records, receipts, prior returns, notices, and entity filings

Ask a short clarifying question when one missing fact changes the likely answer.

## Research Workflow

1. Identify the tax topic and taxpayer posture.
2. Identify the controlling jurisdiction and tax year.
3. Check primary sources first: tax agency pages, statutes, regulations, forms,
   instructions, notices, and official publications.
4. Use secondary sources only to explain or cross-check primary guidance.
5. Note the source, effective date, and any uncertainty.
6. Translate the result into practical next steps, document lists, or questions
   for the user's tax professional.

## Response Shape

For tax research, prefer:

```markdown
## Short Answer
[General answer, with uncertainty if any.]

## Facts Used
[Tax year, jurisdiction, taxpayer type, and assumptions.]

## What To Check
[Official forms, instructions, agency pages, or records to verify.]

## Next Steps
[Practical actions or questions for a CPA/EA/tax attorney.]
```

For tax document organization, prefer:

```markdown
## Needed Documents
[Grouped checklist.]

## Missing Facts
[Questions that affect the answer.]

## Prep Notes
[How to organize records for filing or review.]
```

## Defaults

- If the jurisdiction is not given, ask for it before researching rules.
- If the user is in the United States and no state is given, handle federal tax
  separately and ask which state or local rules matter.
- If the user asks for filing advice, turn it into a fact checklist and a set of
  options to review with a qualified tax professional.
- If the user asks about deadlines, thresholds, forms, or rates, verify current
  official guidance.
