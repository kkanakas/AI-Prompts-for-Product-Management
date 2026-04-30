# Mid-Fi Flow Specification

**Phase:** Prototyping
**Purpose:** Generate a grayscale mid-fidelity flow specification for Figma — screen list, navigation map, component inventory, and interaction states — that resolves information architecture and user flow before color, copy, and visual design are introduced.

## Prompt Template

```
You are a senior product designer helping me write a mid-fidelity flow specification. This spec will be used to build grayscale Figma flows for navigation and IA validation — no color, no final copy, no brand decisions. Using the context below, generate the complete specification.

Feature or flow name: [FEATURE_NAME]
Validated lo-fi screens: [LOFI_SCREENS — list the screen names from a completed lo-fi review, or "starting from scratch"]
User type: [USER_TYPE — the primary persona completing this flow]
Flow entry: [FLOW_ENTRY — where the flow begins]
Flow exit: [FLOW_EXIT — what success looks like and where the user lands]
Key IA decisions already made: [IA_DECISIONS — e.g. "confirmation is a modal, not a full page" or "none yet"]
Platform: [PLATFORM — web app / iOS / Android / responsive web]

---

## Section 1 — Navigation Map

Produce a text-based navigation map showing every screen, transition, and decision point in the flow.

Format:
[FLOW_ENTRY]
  → [trigger / action] → [Screen A]
      → [trigger] → [Screen B]  ← primary path
      → [error trigger] → [Screen B-error]  ← error path
  → [back / cancel] → [FLOW_EXIT or prior screen]

Include:
- All navigation triggers (button tap, form submit, back gesture, timeout, error)
- Decision diamonds where the flow branches
- Back / cancel paths
- Dead ends (screens with no onward navigation — flag these)

---

## Section 2 — Screen Specifications

For each screen in the navigation map, provide a full mid-fi component specification.

**[Screen Name]**

Screen type: [page / modal / drawer / bottom sheet / toast / overlay]
Entry trigger: [what causes this screen to appear]
Exit triggers: [list every action that navigates away from this screen and where it goes]

Component inventory:
| Component | Type | Label / Content | Behavior | State variants |
|---|---|---|---|---|
| [name] | [button / input / dropdown / card / list / table / toggle / etc.] | [placeholder label] | [what happens on interact] | [default, hover, active, disabled, loading] |

Layout structure (describe in plain text — no visual):
- Top area: [what sits here]
- Main content area: [how it is organized — e.g. "two-column card grid", "single scrollable list", "split pane"]
- Sticky / fixed elements: [header, footer bar, floating action button, etc.]
- Scroll behavior: [does this screen scroll? what is fixed?]

Screen-level states:
| State | Trigger | What changes |
|---|---|---|
| Loading | Data fetch in progress | [skeleton screens, spinner, disabled CTAs] |
| Empty | No data to display | [empty state illustration, message, primary CTA] |
| Error | API failure or validation error | [error message location, retry action] |
| Success | Action completed | [confirmation treatment — inline, toast, or full screen] |

IA validation questions for this screen:
- [Question stakeholders or users should answer before moving to hi-fi]

---

## Section 3 — Component Reuse Map

List every component that appears on more than one screen so the Figma file uses a single component with variants rather than duplicated frames.

| Component | Screens it appears on | Key variants needed |
|---|---|---|
| [Component name] | [S1, S3, S5] | [default, disabled, loading, error] |

Flag any component that behaves differently across screens — these need separate components, not variants.

---

## Section 4 — Interaction and Animation Notes

For each non-trivial interaction (transitions that affect user orientation or convey state change), specify:

| Trigger | Source screen | Target screen | Transition type | Duration | Notes |
|---|---|---|---|---|---|
| [action] | [screen] | [screen] | [slide / fade / modal lift / expand / none] | [ms] | [any timing or easing note] |

Keep animations functional: motion should communicate hierarchy or state change, not decorate.

---

## Section 5 — Copy and Content Placeholders

For each screen, list the content slots that need final copy — placeholder labels are acceptable in mid-fi but must be flagged so they are not carried into hi-fi.

| Screen | Content slot | Placeholder used | Copy needed by |
|---|---|---|---|
| [screen] | [page title / CTA label / helper text / error message] | [e.g. "Submit" / "Error occurred"] | [hi-fi handoff / user testing / launch] |

---

## Section 6 — Mid-Fi Review Checklist

Generate the checklist for the PM and designer to complete before moving to hi-fi:
- [ ] Navigation map reviewed with the full team — no dead ends
- [ ] All screen states (loading, empty, error, success) are designed, not assumed
- [ ] Component reuse map is agreed — Figma component library seeded
- [ ] IA validation questions from Section 2 have been answered (user testing or stakeholder sign-off)
- [ ] Copy placeholders are logged — content owner assigned for each slot
- [ ] Prototype links built in Figma for the primary path and at least one error path
- [ ] Usability test plan written before hi-fi work begins
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | Name of the feature or flow | `"Team member invitation and role assignment"` |
| `[LOFI_SCREENS]` | Screens validated in lo-fi, or "starting from scratch" | `"Invite entry, Role selection, Confirmation modal, Success state, Error state"` |
| `[USER_TYPE]` | Primary persona using this flow | `"Workspace admin, first time inviting a team member"` |
| `[FLOW_ENTRY]` | Where the flow begins | `"Settings > Members > Invite button"` |
| `[FLOW_EXIT]` | Where the user lands on success | `"Members list with pending invitation visible"` |
| `[IA_DECISIONS]` | IA decisions already locked | `"Role selection is inline on the invite form, not a separate step"` |
| `[PLATFORM]` | Target platform | `"Responsive web app"` |

## Output Variants

**Usability test script variant** — add to the prompt:
```
After completing the spec, write a moderated usability test script for the mid-fi prototype. Include: a one-paragraph scenario to read aloud to the participant, 3–5 task prompts (avoid leading language), think-aloud instructions, and an observation rubric for each screen — what the facilitator should watch for, what success looks like, and what confusion signals to log.
```

**Figma handoff checklist variant** — add to the prompt:
```
Convert the component inventory and component reuse map into a Figma file setup checklist: which components to create first (by reuse frequency), which variants to define before any screen work begins, and the recommended page structure for the Figma file (e.g. Cover, Navigation Map, Screens, Component Library, Annotations).
```

## Tips

- Mid-fi exists to settle IA and navigation — if color or copy debates start during mid-fi review, redirect; those are hi-fi concerns
- Every screen should have at least one exit trigger; a screen with no way out is a trap for users and a bug for engineers
- The component reuse map is the highest-leverage output for engineering handoff — components identified here become the design system inputs
- Run a navigation map walkthrough with stakeholders before building any Figma frames — it takes 20 minutes and surfaces 80% of the structural objections
- Pair with `02-wireframe-brief.md` as the upstream input and `01-ui-prototype-spec.md` for the coded prototype that follows hi-fi
