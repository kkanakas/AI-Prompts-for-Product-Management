# Generate a PRD for the engineering team

**Phase:** Writing the PRD
**Purpose:** Writing a Product Requirements Document with data and cross referenced sources

##Prompt Template

```
Context: 
We are writing a Product requirement document for [PRODUCT DESCRIPTION] targeting [TARGET MARKET]
We are considering [STRATEGIC QUESTION]
I have attached the following information
 - [ LIST ATTACHED DOCUMENTS: slack messages, emails, meeting transcripts, PDF or Word documents]

 OUTPUTS: 
 Write a 6 pager Amazon style narrative for the [PRODUCT DESCRIPTION]
 The document should include the following sections
 - Problem Alignment 
 - Goals and Non-Goals
 - High Level Approach
 - Key Target Personas
 -Key Milestones
 - User scenarios in the following format
 |Milestone| User Story | 
 | [MILESTONE] | Using the following style : As a Persona, I should be able to do [FUNCTION] given [SITUATION]
 ```

## Placeholders
 |Variable| Description|
 |----|------|
 |`[PRODUCT DESCRIPTION]`| Your current understanding of the problem space|
 |`[STRATEGIC QUESTION]` |  Are we planning to Accelerate a capability, Expand a Capability or simplifying a complex capability or are we doing 2 or all of these capabilities|
 |`[MILESTONE]`|  Breaking down the deliverables into milestones| 
 |`[FUNCTION]`| What functionality should the user accomplish
 |`[SITUATION]`| Given the context of the situation in place for the capability to be true| 

 ## Tips
 - It's OK to write "I don't know" for any section — the AI can help fill gaps
- Ask the AI to challenge your hypotheses, not just confirm them
- See `examples/problem-refinement-example.md` for a worked example
