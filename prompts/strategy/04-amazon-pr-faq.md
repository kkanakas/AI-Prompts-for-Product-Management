# Amazon PR/FAQ Generator

**Phase:** Strategy
**Purpose:** Write an Amazon-style Press Release and FAQ (PR/FAQ) document for a feature or product — the discipline of writing the customer announcement before writing a single line of code, forcing clarity on who the customer is, what problem is solved, and why it matters before any build investment is made.

## Background: What is a PR/FAQ and Why Does It Work?

Amazon requires product teams to write a fictional press release before building anything. The idea is simple: if you cannot write a compelling, specific press release announcing the finished product, you do not yet understand it well enough to build it. The PR/FAQ forces teams to answer the hardest questions early — in writing, before the team, resources, and time are committed.

A PR/FAQ has two parts:
- **The Press Release** — a short, customer-focused announcement written as if the product already exists and is being launched today. Maximum one page. Customers are the audience.
- **The FAQ** — the hard questions the document raises. Two sections: External FAQs (what customers will ask) and Internal FAQs (what leadership, engineering, finance, and legal will ask). No page limit.

The document is read silently at the start of meetings. It is revised — sometimes dozens of times — before a team is funded or a build begins. A document that cannot survive a review meeting should not survive as a product.

## Prompt Template

```
You are a senior Amazon-style product advisor. I am a Product Manager writing a PR/FAQ document for [FEATURE OR PRODUCT NAME] to align my team and leadership before any build investment is made.

Here is my context:

**What I am building:**
[ONE SENTENCE — what the feature or product does in plain language]

**Target customer:**
[WHO THIS IS FOR — be as specific as possible: role, situation, company type, what they are doing or struggling with today]

**The problem:**
[WHAT IS BROKEN, PAINFUL, OR MISSING TODAY — describe the current experience in the customer's language, not product language]

**The solution:**
[HOW THIS RESOLVES THE PROBLEM — what the customer can now do, feel, or achieve that they could not before]

**Key differentiators:**
[WHAT MAKES THIS NOTICEABLY BETTER THAN THE ALTERNATIVES — competitor products, workarounds, or doing nothing]

**Constraints:**
[SCOPE LIMITS, TIMELINE, BUDGET, PLATFORM, OR REGULATORY REQUIREMENTS]

---

Using this input, write a complete Amazon-style PR/FAQ with the following structure. Apply these quality standards throughout:
- Write every sentence as if a customer will read it — no internal jargon, no acronyms, no engineering language
- Every claim must be specific — no vague superlatives ("best", "easiest", "most powerful")
- The press release must fit on one page — ruthless editing is required
- Every FAQ answer must be honest — do not write marketing copy in response to hard questions

---

## PRESS RELEASE

**[CITY, DATE] —**

### Headline
One sentence. States the customer benefit plainly. Answers "so what?" for a customer who has never heard of your product. Does NOT use the product name as the subject. Does NOT use words like "revolutionary", "game-changing", or "seamless".

Format: "[Customer type] can now [do something valuable] with [product name]."

### Subheadline
One sentence. Expands the headline with the specific problem solved or the scale of the benefit.

### Opening Paragraph — The World Before
Paint the current state. Who is the customer? What does their day look like today? What is slow, broken, manual, or missing? Write in the third person. Make it specific enough that the target customer reads it and thinks "that's me". (3–4 sentences)

### Problem Paragraph — The Real Cost
Go deeper on the pain. What does this problem cost the customer — in time, money, risk, frustration, or missed opportunity? What have they tried that has not worked? What do they have to do today to work around it? (3–4 sentences)

### Solution Paragraph — The New Reality
Describe what the customer can now do. What has changed? What does their day look like now? Write in the present tense as if the product exists. Focus entirely on the customer experience — not the technology, not the implementation, not the roadmap. Avoid passive voice. (3–4 sentences)

### Getting Started
One sentence on how easy it is to begin. No technical steps. Focus on speed-to-value.

### Customer Quote
A realistic quote from a named customer persona — include their role and company type. The quote must be specific: it names a real outcome, a real frustration that is now resolved, or a real change in behaviour. Vague quotes like "this has transformed our workflow" are not acceptable. Write as if a journalist will fact-check it.

### Company / PM Quote
A quote from the PM or a company leader framing why this matters strategically — what it enables for customers at scale, or what it represents for the company's direction. Keep it grounded; avoid mission-statement language.

### Boilerplate
One sentence describing the product and company.

### Contact
[Contact name and email placeholder]

---

## FAQ

### External FAQ — Questions customers will ask

Write 8–10 questions a real customer would ask before adopting this feature. Include:
- Questions about what it does and does not do
- Questions about pricing, plan availability, or access
- Questions about data, privacy, or security
- Questions about migration or setup effort
- Questions that express scepticism ("isn't this just...?")
- Questions about what happens when things go wrong

For each question, write a direct, honest answer in plain language. If the answer is "we don't know yet" or "not in v1", say so — do not deflect.

### Internal FAQ — Questions leadership, engineering, finance, and legal will ask

Write 8–10 questions internal stakeholders will raise. Include:
- Why now? Why not earlier or later?
- Who specifically is this for, and how many customers does it affect?
- How does this fit the company strategy?
- What does success look like and how will we measure it?
- What are we explicitly not building, and why?
- What is the cost to build and maintain?
- What are the top three risks, and how are we mitigating them?
- What happens if we are wrong about the core assumption?
- What would make us kill this mid-build?
- What does the competitive landscape look like, and how long do we have before a competitor closes this gap?

For each question, write an honest answer. Hard questions with honest answers build trust. Hard questions with evasive answers destroy it.

---

## PR/FAQ Readiness Score

After writing the document, evaluate it on five dimensions. Score each 1–5 and explain the score in one sentence.

| Dimension | Score (1–5) | What the score means |
|---|---|---|
| **Customer specificity** — could the target customer read the opening paragraph and immediately recognise themselves? | | |
| **Problem clarity** — is the problem described in the customer's language, with a specific cost or consequence? | | |
| **Solution honesty** — does the solution paragraph describe what the customer experiences, not what engineering built? | | |
| **FAQ completeness** — do the FAQs include the hardest questions, answered honestly? | | |
| **Press release discipline** — does the press release fit on one page and avoid every form of jargon and superlative? | | |

For any dimension scoring below 4, identify the specific sentence or section that dragged the score down and rewrite it.

**Overall readiness:** If all five dimensions score 4 or above, the document is ready for a review meeting. If any score below 4, the document needs another revision before it is shared.
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE OR PRODUCT NAME]` | Name of what you are building | "Clearpath Renewal Alerts" |
| `[ONE SENTENCE DESCRIPTION]` | What it does in plain language | "Automatically notifies legal teams 90 days before a contract expires with the renewal terms and counterparty contacts already surfaced" |
| `[TARGET CUSTOMER]` | Specific person in a specific situation | "General Counsel at a 500-person SaaS company managing 80 active vendor contracts" |
| `[THE PROBLEM]` | Current painful experience | "Renewal dates live in a spreadsheet no one consistently checks; legal teams discover approaching renewals when Finance panics about an unwanted auto-renewal" |
| `[THE SOLUTION]` | What the customer can now do | "Receive an alert 90, 60, and 30 days out with the renewal terms, counterparty contacts, and prior negotiation notes already in front of them" |
| `[KEY DIFFERENTIATORS]` | What makes this better than alternatives | "Unlike calendar reminders, alerts include contract context; unlike enterprise CLMs, no setup required" |
| `[CONSTRAINTS]` | Limits on scope | "Email and in-app only in v1; Professional and Enterprise plans; must ship in 6 weeks" |

## Tips

- **Write the headline last** — it is the hardest sentence in the document and almost always wrong on the first attempt; write everything else first, then come back to it
- **The customer quote is your canary** — if you cannot write a specific, believable quote from a real type of customer, you do not know your customer well enough yet; this is a signal to do more discovery before writing the rest
- **Revise, do not polish** — the goal of the first draft is to surface what you do not know; the goal of revision is to answer those unknowns, not to make the language sound better
- **Read it aloud before sharing** — any sentence that sounds like a brochure has not been edited enough
- **The internal FAQ is not a threat** — treating hard questions as attacks leads to evasive answers; the questions exist to make the plan stronger, not to challenge the author
- **One page is a forcing function** — if the press release does not fit on one page, the product is not yet clear enough; cut scope, not words
