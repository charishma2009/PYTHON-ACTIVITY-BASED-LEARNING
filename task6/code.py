

CONSULTATION = 500
DIAGNOSTIC = 1000
CONCESSION_RATE = 0.10

patient_id = input("Enter patient ID: ")
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
treatment = float(input("Enter treatment charge: "))

if age <= 0 or treatment < 0:
    print("Invalid patient details or charges")
    raise SystemExit

total = CONSULTATION + DIAGNOSTIC + treatment

if age >= 60:
    concession = total * CONCESSION_RATE
else:
    concession = 0

final_bill = total - concession

print("\nTotal bill: Rs.", round(total, 2))
print("Concession: Rs.", round(concession, 2))
print("Final bill: Rs.", round(final_bill, 2))

payment = float(input("Enter payment amount: "))

if payment < 0 or payment > final_bill:
    print("Invalid payment amount")
    raise SystemExit

balance = final_bill - payment

if final_bill < 2000:
    category = "Low"
elif final_bill <= 5000:
    category = "Medium"
else:
    category = "High"

print("\n===== HOSPITAL BILL =====")
print("Patient ID:", patient_id)
print("Patient name:", name)
print("Age:", age)
print("Final bill: Rs.", round(final_bill, 2))
print("Amount paid: Rs.", round(payment, 2))
print("Outstanding balance: Rs.", round(balance, 2))
print("Patient classification:", category)

if balance == 0:
    print("Payment status: Fully Paid")
else:
    print("Payment status: Partially Paid")

