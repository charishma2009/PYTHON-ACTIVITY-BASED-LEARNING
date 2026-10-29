

FIXED_CHARGE = 100
INCREASE_LIMIT = 30

n = int(input("Enter number of months: "))

if n <= 0:
    print("Invalid number of months")
    raise SystemExit

bills = []

for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units")
        raise SystemExit

    # Calculate progressive energy charges
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    surcharge = 0
    rebate = 0

    if units > 200:
        surcharge = energy * 0.05
    elif units <= 100:
        rebate = energy * 0.05

    bill = energy + FIXED_CHARGE + surcharge - rebate
    bills.append((units, energy, surcharge, rebate, bill))

print("\n===== ELECTRICITY BILL REPORT =====")

for i, record in enumerate(bills):
    units, energy, surcharge, rebate, bill = record

    print(f"\nMonth {i + 1}")
    print(f"Units consumed: {units:.2f}")
    print(f"Energy charge: Rs. {energy:.2f}")
    print(f"Fixed charge: Rs. {FIXED_CHARGE:.2f}")
    print(f"Surcharge: Rs. {surcharge:.2f}")
    print(f"Rebate: Rs. {rebate:.2f}")
    print(f"Final bill: Rs. {bill:.2f}")

    if i > 0:
        previous_bill = bills[i - 1][4]
        change = ((bill - previous_bill) / previous_bill) * 100

        print(f"Monthly change: {change:.2f}%")

        if change > INCREASE_LIMIT:
            print("Warning: Unusual bill increase!")
        elif change < 0:
            print("Bill decreased")
        else:
            print("No unusual increase")

