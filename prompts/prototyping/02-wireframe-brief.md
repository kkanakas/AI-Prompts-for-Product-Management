# Lo-Fi Wireframe Brief

**Phase:** Prototyping
**Purpose:** Generate a structured wireframe brief — screen inventory, information architecture, and per-screen annotation — that a PM can hand directly to a designer or use to build lo-fi wireframes in Balsamiq, Whimsical, or FigJam.

## Prompt Template

```
You are a product designer helping me create a lo-fi wireframe brief for a new feature or flow. Using the context below, generate a complete wireframe brief I can hand to a designer or use in Balsamiq or Whimsical.

Feature or flow name: [FEATURE_NAME]
Product context: [PRODUCT_CONTEXT — what the product does, who uses it, what platform (web, mobile, desktop)]
User goal: [USER_GOAL — what the user is trying to accomplish in this flow]
Entry point: [ENTRY_POINT — where the user starts, e.g. "dashboard home page", "email notification", "navigation menu"]
Success state: [SUCCESS_STATE — what the user sees or can do when the flow completes successfully]
Known constraints: [CONSTRAINTS — e.g. "must work on mobile", "existing nav structure cannot change", "must not require login for first step", or "none"]

---

## Section 1 — Screen Inventory

List every screen (or significant modal/drawer state) needed to complete this flow from entry point to success state. For each screen:

| Screen ID | Screen name | Purpose | Triggered by | Leads to |
|---|---|---|---|---|
| S1 | [name] | [what the user does here] | [what action opens this screen] | [S2, S3, or exit] |

Include:
- All primary path screens (happy path)
- Key error states (validation failure, empty state, not-found)
- Any confirmation or success screens

---

## Section 2 — Information Architecture

Draw the navigation structure as a simple outline (not a diagram — text-only hierarchy):

Entry point
└── S1: [Screen name]
    ├── S2: [Screen name — primary path]
    │   └── S3: [Screen name]
    └── S4: [Screen name — error / alternative path]

Flag any IA decisions that need validation with users (e.g. "Should the confirmation step be a modal or a full page?").

---

## Section 3 — Per-Screen Annotation

For each screen in the inventory, produce a wireframe annotation in this format:

**[Screen ID]: [Screen name]**

Layout zones:
- Header: [what appears — e.g. "page title, back navigation, primary CTA"]
- Body: [main content — list each section or component]
- Footer / actions: [buttons, links, or persistent navigation]

Components on this screen:
| Component | Type | Content / label | Notes |
|---|---|---|---|
| [name] | [button / input / card / table / etc.] | [label or content] | [behavior, validation, or state notes] |

States to design:
- Default: [what the screen looks like on first load]
- Loading: [if async data — what shows while waiting]
- Empty: [if no data — what message or CTA appears]
- Error: [if something fails — what the user sees]
- Success: [if applicable — confirmation state]

Open questions for this screen:
- [Any layout, content, or IA question that needs a decision before wireframing]

---

## Section 4 — Out of Scope

List any related screens or interactions that are explicitly NOT included in this wireframe brief, and why:

| Out of scope | Reason |
|---|---|
| [Screen or interaction] | [e.g. "addressed in a separate flow", "post-MVP", "handled by existing component"] |

---

## Section 5 — Wireframe Review Checklist

Generate a short checklist the PM and designer should walk through before moving to mid-fi:
- [ ] All screens in the inventory are accounted for
- [ ] Every screen has a clear entry point and at least one exit
- [ ] Error states and empty states are annotated for all data-dependent screens
- [ ] IA decisions flagged in Section 2 have been resolved
- [ ] Out-of-scope items are agreed and documented
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[FEATURE_NAME]` | Name of the feature or flow being wireframed | `"Onboarding checklist for new workspace members"` |
| `[PRODUCT_CONTEXT]` | What the product does and who uses it | `"B2B SaaS project management tool used by engineering teams; web app"` |
| `[USER_GOAL]` | What the user is trying to accomplish | `"Complete account setup and invite their first team member within 10 minutes of signing up"` |
| `[ENTRY_POINT]` | Where the user enters the flow | `"Post-signup landing page after email verification"` |
| `[SUCCESS_STATE]` | What the user sees when they finish | `"Dashboard with first project created and team invitation sent"` |
| `[CONSTRAINTS]` | Hard constraints on the design | `"Must work on mobile; cannot change the existing top navigation"` |

## Output Variants

**Mobile-first variant** — add to the prompt:
```
This wireframe is for a native mobile app (iOS/Android). Replace all layout zones with mobile-native patterns: tab bar navigation instead of sidebar, bottom sheet instead of modal, swipe gestures instead of button rows. Annotate thumb-reach zones — flag any primary action that falls outside the comfortable thumb zone on a standard phone screen.
```

**Annotated user story variant** — add to the prompt:
```
For each screen, add a "User story" field in the annotation: "As a [user type], I want to [action], so that [outcome]." This links each screen directly to a sprint-ready story and makes the wireframe brief usable as an input to a backlog grooming session.
```

## Tips

- Lo-fi is about structure, not aesthetics — resist the urge to describe colors, fonts, or icons; focus on layout zones and component types
- Empty states are the most commonly skipped annotation; a missing empty state almost always becomes a bug in development
- The IA outline in Section 2 is the fastest way to spot missing screens — walk it as a user before handing off to design
- Pair with `03-mid-fi-flow-spec.md` once the IA is validated — lo-fi resolves structure, mid-fi resolves navigation and component behavior
