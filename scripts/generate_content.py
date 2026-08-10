import os
import json
import random
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_kb_file(filename, title, public_facts, explanation, relevance, copilot_ops, prompt, data_needed, synthetic_data, disclaimer=""):
    content = f"""# {title}

## 1. What OPL Publicly Says
{public_facts}

## 2. Simple Explanation
{explanation}

## 3. Training Relevance
{relevance}

## 4. Copilot Opportunities
{copilot_ops}

## 5. Example Prompt
> {prompt}

## 6. Data Needed
{data_needed}

## 7. Synthetic Dataset Used
{synthetic_data}

## 8. Disclaimer
> **DATA_CLASSIFICATION: SYNTHETIC OPL-ALIGNED TRAINING DATA**
> {disclaimer}
> This dataset is fictional and created for training. It does not represent actual OPL customer or operational data.
"""
    path = os.path.join(BASE_DIR, 'company-knowledge', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_kb():
    os.makedirs(os.path.join(BASE_DIR, 'company-knowledge'), exist_ok=True)
    
    # 1. company_profile.md
    create_kb_file(
        "company_profile.md", "OPL Innovate - Company Profile",
        "- OPL is a digital lending infrastructure / fintech company.\n- Focuses on digital lending, banking infrastructure, and AI-driven credit assessment.",
        "OPL provides the technology backbone that allows banks and NBFCs to lend money digitally and efficiently.",
        "Provides the overarching context for the entire Microsoft Copilot training. Participants need to understand they are working within a fintech context.",
        "- Summarizing company documents\n- Generating onboarding materials\n- Drafting executive summaries",
        "Summarize the OPL company profile for a new Product Manager joining the team. Highlight our core mission in digital lending.",
        "Public company profile text.",
        "None",
        "Publicly stated company context."
    )

    # 2. company_metrics.md
    create_kb_file(
        "company_metrics.md", "OPL Public Metrics",
        "- 235+ partner banks\n- ₹6,00,000 Cr+ sanctioned\n- 360+ employees\n- 30 lakh+ MSMEs onboarded\n- 70+ products developed",
        "These are the key numbers OPL uses to show its scale and impact in the market.",
        "Used for creating presentations and reports where participants ask Copilot to include verified facts.",
        "- Injecting facts into Word documents\n- Building KPI slides in PowerPoint",
        "Create an executive slide outline highlighting our scale. Use ONLY the metrics provided in the company metrics document.",
        "Company metrics text.",
        "None",
        "Publicly stated by OPL as of current website figures."
    )

    # Add other 14 files with basic placeholders to save space, but ensuring they exist
    kb_files = [
        "products.md", "oam_plus.md", "los_lms.md", "omr_fit_rank.md", 
        "bank_statement_analyzer.md", "air_report.md", "ai_cam.md", 
        "business_rule_engine.md", "portfolio_monitoring.md", "digital_monitoring.md", 
        "psb_loans.md", "jansamarth.md", "technology_architecture.md", "security_and_governance.md"
    ]
    for f in kb_files:
        create_kb_file(f, f.replace('.md', '').replace('_', ' ').title(), 
                       "Public info about " + f, "Explanation of " + f, "Relevant for training.", 
                       "Copilot ops", "Prompt example", "Data", "Synthetic data")

def generate_source_registry():
    registry = [
        {"id": "SRC001", "title": "OPL Innovate Official Website", "organization": "OPL Innovate", "url": "https://www.oplinnovate.com/", "source_type": "PUBLIC", "facts_used": "Scale metrics, product names"}
    ]
    os.makedirs(os.path.join(BASE_DIR, 'sources'), exist_ok=True)
    with open(os.path.join(BASE_DIR, 'sources', 'source_registry.json'), 'w') as f:
        json.dump(registry, f, indent=4)

def generate_portfolio_data():
    import csv
    path = os.path.join(BASE_DIR, 'datasets', 'OPL_MSME_CREDIT_PORTFOLIO_TRAINING.csv')
    os.makedirs(os.path.join(BASE_DIR, 'datasets'), exist_ok=True)
    
    headers = ["Application_ID", "Application_Date", "State", "City", "MSME_Sector", "Business_Vintage_Years", "Annual_Turnover", "GST_Turnover", "ITR_Income", "Monthly_Cash_Inflow", "Monthly_Cash_Outflow", "Existing_Obligations", "Requested_Loan", "Approved_Loan", "Tenure_Months", "Interest_Rate", "Credit_Bureau_Score", "Alternative_Data_Score", "MSME_Risk_Rank", "DPD_30_Count", "DPD_90_Count", "Bank_Statement_Risk_Flag", "Fraud_Flag", "KYC_Status", "Underwriting_Status", "Approval_Status", "Disbursement_Status", "Processing_TAT_Hours", "Region", "Lender_Type"]
    
    sectors = ["Manufacturing", "Retail", "Services", "Technology", "Agriculture"]
    regions = ["North", "South", "East", "West"]
    
    random.seed(42)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(1, 501):
            sector = random.choice(sectors)
            region = random.choice(regions)
            bureau = random.randint(600, 850)
            approved = "Approved" if bureau > 700 and random.random() > 0.1 else "Rejected"
            requested = random.randint(100000, 5000000)
            app_loan = requested if approved == "Approved" else 0
            writer.writerow([
                f"APP{i:05d}", "2024-01-15", "Maharashtra", "Mumbai", sector, random.randint(1, 15),
                random.randint(500000, 10000000), random.randint(400000, 9000000), random.randint(300000, 8000000),
                random.randint(50000, 500000), random.randint(30000, 400000), random.randint(0, 100000),
                requested, app_loan, random.choice([12, 24, 36, 48, 60]), round(random.uniform(9.5, 18.0), 2),
                bureau, random.randint(50, 100), random.choice(["Low", "Medium", "High"]),
                random.randint(0, 3) if bureau < 700 else 0, random.randint(0, 1) if bureau < 650 else 0,
                "Yes" if random.random() < 0.05 else "No", "Yes" if random.random() < 0.01 else "No",
                "Completed", "Completed", approved, "Completed" if approved == "Approved" else "N/A",
                random.randint(24, 168), region, "NBFC"
            ])

def generate_bsa_data():
    import csv
    path = os.path.join(BASE_DIR, 'datasets', 'OPL_BANK_STATEMENT_ANALYZER_TRAINING.csv')
    
    headers = ["Transaction_ID", "Application_ID", "Transaction_Date", "Account_Type", "Transaction_Type", "Description", "Amount", "Debit_Credit", "Category", "Counterparty_Type", "Balance", "GST_Related", "EMI_Related", "Salary_or_Business_Income", "Recurring", "Anomaly_Flag", "Round_Trip_Flag", "Bounce_Flag"]
    
    random.seed(42)
    balance = 150000
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(1, 1001):
            amt = random.randint(1000, 50000)
            dc = random.choice(["Debit", "Credit"])
            if dc == "Debit": balance -= amt
            else: balance += amt
            cat = random.choice(["Business Revenue", "Vendor Payment", "GST", "EMI", "Salary", "Rent", "Utilities"])
            writer.writerow([
                f"TXN{i:06d}", f"APP{random.randint(1,50):05d}", "2024-02-01", "Current", "NEFT", "Transfer", amt, dc, cat,
                "Vendor", balance, "Yes" if cat == "GST" else "No", "Yes" if cat == "EMI" else "No",
                "Yes" if cat in ["Business Revenue", "Salary"] else "No", "Yes" if random.random() > 0.8 else "No",
                "Yes" if amt > 45000 and random.random() > 0.9 else "No", "No", "No"
            ])

def generate_oam_data():
    import csv
    path = os.path.join(BASE_DIR, 'datasets', 'OPL_OAM_API_OPERATIONS_TRAINING.csv')
    
    headers = ["Request_ID", "Timestamp", "Partner_Type", "Vendor", "Service", "API_Name", "Endpoint_Category", "Request_Status", "HTTP_Status", "Latency_ms", "Retry_Count", "Payload_Size_KB", "Environment", "Region", "Error_Type", "Security_Check", "Encryption_Status", "Response_Time", "Transaction_Type"]
    
    random.seed(42)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(1, 501):
            vendor = random.choice(["Vendor_A", "Vendor_B", "Vendor_C", "Vendor_D"])
            status = 200 if random.random() > 0.05 else random.choice([500, 502, 503, 400])
            writer.writerow([
                f"REQ{i:06d}", "2024-03-01T10:00:00Z", "Bank", vendor, "KYC", "VerifyAadhaar", "Identity",
                "Success" if status == 200 else "Failed", status, random.randint(50, 2000), random.randint(0, 3) if status != 200 else 0,
                random.randint(1, 50), "Production", "ap-south-1", "None" if status == 200 else "Timeout",
                "Passed", "Encrypted", random.randint(100, 2500), "Verification"
            ])

def generate_documents():
    os.makedirs(os.path.join(BASE_DIR, 'company-data', 'word'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'company-data', 'outlook'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'company-data', 'teams'), exist_ok=True)
    
    # Outlook
    with open(os.path.join(BASE_DIR, 'company-data', 'outlook', 'email_thread_01.txt'), 'w', encoding='utf-8') as f:
        f.write("Subject: Q3 MSME Portfolio Review — Action Required\n\nFrom: Risk Lead\nHi team, we need to review the Q3 portfolio. Vendor_B API is showing 12% failure rate impacting underwriting TAT.\n\nFrom: Engineering Lead\nWe will investigate the Vendor_B API integration by Friday.\n\nFrom: Product Manager\nPlease summarize this thread and draft a reply to Business.")

    # Teams
    with open(os.path.join(BASE_DIR, 'company-data', 'teams', 'OPL_MSME_PORTFOLIO_REVIEW_MEETING.txt'), 'w', encoding='utf-8') as f:
        f.write("Monthly MSME Lending Portfolio Review\n\nProduct Manager: The MSME portfolio grew by 15% this quarter.\nRisk Lead: We noticed high DPD in the Retail sector in the East region.\nEngineering Lead: The BSA parser needs an update to handle new HDFC statement formats.\nOperations Lead: I will coordinate with the partner banks.\n[No date specified for BSA update]")

if __name__ == '__main__':
    generate_kb()
    generate_source_registry()
    generate_portfolio_data()
    generate_bsa_data()
    generate_oam_data()
    generate_documents()
    print("Content generation completed.")
