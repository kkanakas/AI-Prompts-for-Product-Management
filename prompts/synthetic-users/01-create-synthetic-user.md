# Create Synthetic Users

**Phase:** Synthetic Users
**Purpose:** Generate realistic AI personas to simulate customer responses before real interviews.

## Prompt Template

```
Create a synthetic user that describes a member of the customer segment
I have chosen. Be as specific as possible in your description.

INPUTS:
[PROBLEM STATEMENT]
[CUSTOMER SEGMENT DESCRIPTION]

OUTPUT:
A description of the user structured to cover the following information:
- About me (name, age, job/profession)
- My motivations and goals (regarding the specific problem statement)
- Describe my typical day
- My needs and problems-to-solve
- My frustrations with current situation and solutions
```

### For B2B Users — Add These Fields

```
Additional characteristics:
- Role (specific job title and responsibilities)
- Company information (company size, industry, team structure)
- Current solution (what they use today)
- Constraints (budget, time, technical limitations)
```

## Placeholders

| Variable | Description |
|---|---|
| `[PROBLEM STATEMENT]` | The problem you're exploring |
| `[CUSTOMER SEGMENT DESCRIPTION]` | Demographics, role, context of your target users |

## Tips

- Create 3-5 synthetic users to cover different sub-segments
- Synthetic users are for hypothesis generation, not validation — always follow up with real users
