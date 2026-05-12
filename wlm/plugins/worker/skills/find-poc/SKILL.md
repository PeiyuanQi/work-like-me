---
name: find-poc
description: Use when user needs to find a person of contact for any type of request - reimbursement approvals, PTO requests, team questions, customer contacts, vendor contacts, budget approvals, or any "who should I ask" type questions. NOT for code review - use swe:find-code-reviewer for that.
---

# Find Person of Contact (Generalized)

Version: 1.0.0

Find the appropriate person to contact for any type of request across the organization.

## When to Use

- User asks: "who approves", "who handles", "who should I ask", "who do I contact"
- Need POC for: reimbursements, PTO, customer questions, vendor contacts, budget, team-specific questions
- Any non-code-review POC request

**DO NOT USE for code review** - use `swe:find-code-reviewer` instead.

## Step 1: Clarify the Request (if needed)

If the request type is unclear, ask clarifying questions:
- "Is this for code review?" → Use swe:find-code-reviewer
- "What type of request is this?" (reimbursement, PTO, customer, vendor, team question)

## Step 2: Determine POC Category

Map the request to a POC type:

| Request Type | Search For |
|--------------|------------|
| Reimbursement/Expenses | Finance team, expense approvers, managers |
| PTO/Time Off | HR, manager, PTO policy |
| Customer/Client | Account manager, customer success, sales |
| Vendor/Supplier | Procurement, vendor manager |
| Budget/Approval | Finance, department head, budget owner |
| Team Question | Team lead, subject matter expert |
| Security/Security | Security team, IT |
| IT/Technical | IT support, tech lead |

## Step 3: Search Memory

**REQUIRED SUB-SKILL:** Use worker:search-memory to find team and role information.

Search for:
- Team structure and roles
- Specific role directories (e.g., `memory/teams/roles/`)
- Policy files (reimbursement, PTO, etc.)
- Contact lists or rosters

**Memory search patterns by POC type:**
- `memory/teams/*/roles/*` - Role-based contacts
- `memory/teams/*/poc/*` - Point of contact files
- `memory/corps/tools/*` - Company-wide tool contacts
- `memory/projects/*/contacts*` - Project contacts

## Step 4: Check for Role Directories

Look for structured role-based directories:
- `memory/teams/roles/approvers/` - Approval POCs
- `memory/teams/roles/finance/` - Finance team contacts
- `memory/teams/roles/hr/` - HR contacts
- `memory/corps/policies/` - Policy documents with POC info

## Step 5: Determine Best Contact

Based on findings, determine:
- **Name:** Person to contact
- **Role:** Their role/title
- **Contact method:** Best way to reach them (Slack, Teams, Email)
- **Why:** Brief explanation of why they're the right person

## Step 6: Return Results

Format the results:
```markdown
# Person of Contact

**Type:** [Reimbursement/PTO/Customer/Team Question/etc.]
**Name:** [Name]
**Role:** [Role]
**Best Contact:** [Slack/Teams/Email]
**Why:** [Why they're the right person]
```

## Fallback

If no clear POC found:
- Ask the user for clarification or their preference
- Suggest checking with their direct manager
- Suggest checking the company directory
