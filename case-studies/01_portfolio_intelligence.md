# Case Study 1: MSME Credit Portfolio Intelligence

**Question:** "Where is portfolio risk increasing?"

## Context
OPL Innovate provides MSME credit intelligence. Our portfolio monitoring tools allow banks to assess the health of their lending book in real-time.

## Problem
The Q3 portfolio report shows a slight increase in 30+ DPD (Days Past Due), but the operations team cannot identify which region or sector is driving this without manual analysis.

## Dataset
`OPL_MSME_CREDIT_PORTFOLIO_TRAINING.csv`
> **[SYNTHETIC OPL-ALIGNED DATA]**

## Copilot Prompts
1. "Analyze the attached portfolio data and identify which region has the highest 30+ DPD count."
2. "Is there a correlation between the Business Vintage Years and the MSME Risk Rank?"
3. "Create a bar chart showing the average Approved Loan amount by Sector."

## Expected Insights
- High 30+ DPD is concentrated in the Retail sector in the East region.
- Lower Business Vintage correlates with High MSME Risk Rank.

## Business Decision
Tighten underwriting rules (using the Business Rule Engine) for new Retail applications in the East region with vintage < 3 years.

## Verification
- Does the chart exactly match the Excel pivot table?
- Did Copilot hallucinate any data points?
