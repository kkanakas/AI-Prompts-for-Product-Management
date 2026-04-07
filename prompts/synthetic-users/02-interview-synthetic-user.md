# Interview Synthetic Users

**Phase:** Synthetic Users
**Purpose:** Have AI role-play as a UX Researcher interviewing your synthetic persona.

## Prompt Template

```
You are role-playing as a UX Researcher.
Conduct an interview with my synthetic user following the interview guide
provided. I would like you to listen attentively to what the user has to say,
especially around problems, needs, and frustrations with the current situation.
What is standing out? What is important to the user? How is the user trying
to address the problem? What is the impact?
I don't want you to follow the interview script to the letter. If the synthetic
user mentions something unexpected or particularly interesting, I'd like for
you to explore that area and learn more.

INPUT:
- The problem statement: [PROBLEM STATEMENT]
- The description of the synthetic user: [SYNTHETIC USER]
- The interview guide: [INTERVIEW GUIDE]

OUTPUT:
Collect the responses from the interview (transcript).
Highlight the following areas:
- What does the user say about the problem?
- What does the user think?
- What does the user feel?
- What does the user do?
- What do they struggle with?
- What are the user's most pressing needs?
- In what other ways are they solving the problem today?
- Surprise (What did you discover? Was there anything unexpected or surprising?)

IMPORTANT:
- If you don't have enough information to answer authentically, say
  "I don't know" or "I need to understand my specific situation better"
- Don't make up specific details not grounded in real user patterns
- Challenge assumptions in my questions if they seem wrong for this user
```

### Follow-Up Probes

After the interview, try these follow-ups:

```
You mentioned [RESPONSE]. Can you tell me more about why that matters?
Walk me through the last time you experienced this.
What have you tried to solve this?
How much does this problem cost you (time/money/frustration)?
```

## Placeholders

| Variable | Description |
|---|---|
| `[PROBLEM STATEMENT]` | The problem being explored |
| `[SYNTHETIC USER]` | Full persona description (from 01-create-synthetic-user) |
| `[INTERVIEW GUIDE]` | Your prepared interview questions (from 01-interview-guide) |
