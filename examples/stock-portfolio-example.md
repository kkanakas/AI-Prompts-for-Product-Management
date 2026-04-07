# Example: Stock Portfolio Viewer Prototype

This is a worked example of the UI Prototype Spec prompt (`prompts/prototyping/01-ui-prototype-spec.md`).

## Filled-In Prompt

```
I need a web application prototype for a personal stock portfolio dashboard.

TARGET USERS: Individual investors who want to quickly understand their
portfolio performance without opening their brokerage app

CORE FUNCTIONALITY:
1. Display a list of stocks the user owns with key information for each
2. Show growth percentage with clear visual indicators (green for gains,
   red for losses)
3. Allow users to sort the list by stock name (alphabetically) or by
   growth percentage (highest to lowest or vice versa)
4. Display total portfolio value and overall portfolio growth at the top

KEY INTERACTIONS:
- When users click on column headers (Stock Name, Growth %), the list
  should sort by that column
- Clicking the same header again should reverse the sort order
  (ascending/descending)
- Growth percentages should be color-coded: green for positive, red for
  negative, gray for zero
- Hovering over a stock row should highlight it to show it is interactive
- The total portfolio summary at the top should dynamically update based
  on the sample data

DATA/CONTENT:
- Create a portfolio of 8-10 diverse stocks with realistic data:
  * Mix of tech stocks (like AAPL, MSFT, GOOGL)
  * Some traditional stocks (like JNJ, WMT)
  * Include both winners and losers in the portfolio
  * Sample growth percentages ranging from -15% to +35%
  * Share counts and current prices that feel realistic
- Show: Stock Symbol, Company Name, Shares Owned, Current Price,
  Total Value, Growth %
- Portfolio total should be around $50,000-$100,000

VISUAL STYLE:
- Professional and clean, like a financial dashboard
- Use a dark theme with lighter text (financial apps often use this)
- Green (#00ff00) for positive growth
- Red (#ff0000) for negative growth
- Use clear typography - numbers should be easy to scan
- Add subtle borders or cards to separate stocks visually
- Make growth percentages prominent and easy to spot

TECHNICAL NOTES:
- Make sorting fully functional with visual indicators (arrows) showing
  current sort direction
- Calculate and display the total portfolio value and overall growth
  percentage
- Format currency values with $ and commas (e.g., $1,234.56)
- Format percentages with + or - signs (e.g., +12.5%, -3.2%)
- Make it responsive for both desktop and mobile viewing
- Use a table or card layout that's easy to scan quickly
```

## What to Notice

- Every section is filled with specific, concrete details
- Sample data is described with realistic ranges and variety
- Visual style includes exact hex colors and specific UI behaviors
- Technical notes cover formatting, sorting mechanics, and responsiveness
