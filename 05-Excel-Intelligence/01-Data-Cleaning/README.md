# 01 - Data Cleaning Scope & Audit Notes

Complements the top-level [Excel Intelligence README](../README.md) by focusing on dataset structure, edge cases, and handoff checks rather than repeating formula definitions or summary KPIs.

## Raw Input Audit (`Customers_Messy.csv`)
- **Source Schema (7 Columns):** `FullName`, `Email`, `Phone`, `City`, `State`, `PIN`, `LifetimeSpend`.
- **Row-Level Findings (6 Raw Rows):**
  - **Rows 1-5:** Retained as valid customer records after normalizing spacing, casing, phone formatting, and numeric spend values.
  - **Row 6:** Dropped as an unrecoverable record (`bad.email@@example..com`, `indecipherable`, and missing `State`, `PIN`, and `LifetimeSpend`).

## Edge Cases & Quality Checks
- **Inconsistent Number Formats:** `LifetimeSpend` mixed comma-separated strings (e.g., `1,20,000`, `72,500`, `1,50,000`, `99,999`) with plain numeric text (`85000`).
- **Phone Prefix Variations:** Raw entries included `+91`, `091`, and `098` prefixes alongside mixed spaces, hyphens, and plain 10-digit strings (`9876543210`).
- **Post-Clean Verification:** Confirmed zero blank `Customer_Tier` labels, numeric-only spend values ready for aggregation, and local-only storage for `.xlsx` workbooks.