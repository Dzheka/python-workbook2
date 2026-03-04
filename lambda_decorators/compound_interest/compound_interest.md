#  **Topic:** Bank | **Concept:** Recursion

Write a **recursive** function `compound_interest(principal, rate, years)` that calculates compound interest year by year.

Rules:
- Base case: `years == 0` → return `principal`
- Each year: `principal *= (1 + rate)`
- Round the final result to 2 decimal places
- **No loops allowed**