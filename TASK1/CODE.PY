
balance = 5000
max_withdrawal = 10000

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)
    transaction = input("Enter type (D/W): ").upper()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Rejected: Invalid amount")
        rejected += 1

    elif transaction == "D":
        balance += amount
        total_deposits += amount
        successful += 1
        print("Deposit successful")

    elif transaction == "W":
        if amount > max_withdrawal:
            print("Rejected: Withdrawal limit exceeded")
            rejected += 1

        elif amount > balance:
            print("Rejected: Insufficient balance")
            rejected += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful += 1
            print("Withdrawal successful")

    else:
        print("Rejected: Invalid transaction type")
        rejected += 1

print("\n----- ATM TRANSACTION SUMMARY -----")
print(f"Total deposits: Rs. {total_deposits:.2f}")
print(f"Total withdrawals: Rs. {total_withdrawals:.2f}")
print(f"Successful transactions: {successful}")
print(f"Rejected transactions: {rejected}")
print(f"Final balance: Rs. {balance:.2f}")

