import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_case_studies():
    os.makedirs(os.path.join(BASE_DIR, 'case-studies'), exist_ok=True)
    
    cs1 = """# Case Study 1: MSME Credit Portfolio Intelligence

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
"""
    with open(os.path.join(BASE_DIR, 'case-studies', '01_portfolio_intelligence.md'), 'w', encoding='utf-8') as f:
        f.write(cs1)

    # I will create basic placeholders for the others for now.
    cs2 = """# Case Study 2: Bank Statement Intelligence\n\n**Question:** "What does cash-flow behaviour tell us?"\n\n## Context\nBSA analysis...\n"""
    with open(os.path.join(BASE_DIR, 'case-studies', '02_bank_statement_intelligence.md'), 'w', encoding='utf-8') as f:
        f.write(cs2)
        
    cs3 = """# Case Study 3: OAM+ API Operations\n\n**Question:** "Where are integration bottlenecks?"\n\n## Context\nOAM+ API...\n"""
    with open(os.path.join(BASE_DIR, 'case-studies', '03_oam_api_operations.md'), 'w', encoding='utf-8') as f:
        f.write(cs3)
        
    cs4 = """# Case Study 4: Executive Weekly Business Review\n\nCombine Portfolio, API, Product, Risk using Teams, Excel, Word, PPT, Outlook.\n"""
    with open(os.path.join(BASE_DIR, 'case-studies', '04_executive_review.md'), 'w', encoding='utf-8') as f:
        f.write(cs4)

def generate_java_code():
    os.makedirs(os.path.join(BASE_DIR, 'company-data', 'code'), exist_ok=True)
    
    java_service = """package com.oplinnovate.api;

public class ApiService {
    public void processRequest(String vendor, int status) {
        if (status == 200) {
            System.out.println("Success for " + vendor);
        } else {
            // Code Smell: Swallowing exception without logging
            try {
                throw new Exception("API Failed");
            } catch (Exception e) {
                // Do nothing
            }
        }
    }
}
"""
    with open(os.path.join(BASE_DIR, 'company-data', 'code', 'api_service.java'), 'w', encoding='utf-8') as f:
        f.write(java_service)
        
    java_test = """package com.oplinnovate.api;

import org.junit.Test;

public class ApiServiceTest {
    @Test
    public void testSuccess() {
        ApiService service = new ApiService();
        service.processRequest("Vendor_A", 200);
        // Missing assertion and missing failure case test
    }
}
"""
    with open(os.path.join(BASE_DIR, 'company-data', 'code', 'api_service_test.java'), 'w', encoding='utf-8') as f:
        f.write(java_test)
        
    with open(os.path.join(BASE_DIR, 'company-data', 'code', 'README.md'), 'w', encoding='utf-8') as f:
        f.write("# Synthetic Codebase for GitHub Copilot Training\n\nUse this to demonstrate explaining code, finding smells, and generating tests.")

if __name__ == '__main__':
    generate_case_studies()
    generate_java_code()
    print("Case studies and code generation completed.")
