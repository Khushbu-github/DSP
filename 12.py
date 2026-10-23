"""
Experiment 12: Case Study on GDPR and DPDP Act 2023
Create a comparative chart of GDPR and DPDP Act 2023 principles and
explain roles like Data Protection Officer (DPO). Include a mock
incident report format.
"""
import datetime

# GDPR vs DPDP
data = [
    ("Jurisdiction", "EU", "India"),
    ("Consent", "Clear consent", "Clear consent"),
    ("DPO", "Required in certain cases", "Required for Significant Data Fiduciaries"),
    ("Breach", "72 hours", "Without delay"),
    ("Penalty", "Up to €20M / 4%", "Up to ₹250 crore"),
    ("Rights", "Access, erase, rectify", "Access, correct, erase")
]

print("GDPR vs DPDP Act 2023")

for a, gdpr, dpdp in data:
    print("\n", a)
    print("GDPR :", gdpr)
    print("DPDP :", dpdp)

# DPO role
print("""
DPO Role:
1. Monitor data protection
2. Ensure legal compliance
3. Handle user requests
4. Contact the regulator
5. Advise on privacy risks
""")

# Mock incident report
print("\nDATA BREACH INCIDENT REPORT")
print("Date:", datetime.datetime.now())
print("Incident: Unauthorized access")
print("Data: Names and emails")
print("Affected Records: 500")
print("Cause: Weak access control")
print("Action: Access revoked and system isolated")
print("Plan: Enable MFA and improve security")