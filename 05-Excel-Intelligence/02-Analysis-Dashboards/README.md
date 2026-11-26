# 02 - Excel PivotTable & Secondary-Axis Chart Analysis

Complements the main [Excel Intelligence README](../README.md) by documenting the aggregation structure, PivotTable field mappings, and visualization choices.

## Analysis Setup & Aggregation
- **Data Source:** Cleaned dataset derived from `Customers_Messy.csv` (`n = 5` valid customer records).
- **PivotTable Fields:**
  - **Rows:** `Customer_Tier` (`High Value`, `Medium Value`, `Standard`)
  - **Values:** `Sum of Clean_Spend` (formatted as Currency), `Count of FullName` (Customer Count)

## Visual Design & KPI Highlights
- **Chart Type:** Secondary-axis PivotChart pairing spend volume with customer density across tiers.
- **Key Insight:** `High Value` and `Medium Value` tiers hold equal customer volume (`2` each), but `High Value` generates `270,000` (`51.2%` of total revenue) compared to `184,999` (`35.1%`) from `Medium Value`.
- **Asset Reference:** See visual output at `../assets/pivottable_tier_summary.png`.