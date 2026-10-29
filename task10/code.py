

FINE_PER_DAY = 5
records = []

n = int(input("Enter number of borrowing records: "))

if n <= 0:
    print("Invalid number of records")
    raise SystemExit

for i in range(n):
    print("\nRecord", i + 1)

    book_id = input("Enter book ID: ")
    borrowing_days = int(input("Enter borrowing period in days: "))
    delay = int(input("Enter return delay in days: "))
    returned = input("Has the book been returned? (yes/no): ").lower()

    if borrowing_days <= 0 or delay < 0 or returned not in ["yes", "no"]:
        print("Invalid borrowing record")
        raise SystemExit

    record = (book_id, borrowing_days, delay, returned)
    records.append(record)

total_fine = 0
overdue_count = 0

print("\n===== LIBRARY RECONCILIATION REPORT =====")

for book_id, borrowing_days, delay, returned in records:
    fine = delay * FINE_PER_DAY
    total_fine += fine

    if delay > 0:
        overdue_status = "Overdue"
        overdue_count += 1
    else:
        overdue_status = "On time"

    if returned == "yes":
        availability = "Available"
    else:
        availability = "Not available"

    print("\nBook ID:", book_id)
    print("Borrowing period:", borrowing_days, "days")
    print("Return delay:", delay, "days")
    print("Fine: Rs.", fine)
    print("Status:", overdue_status)
    print("Availability:", availability)

print("\n===== SUMMARY =====")
print("Total records:", len(records))
print("Overdue records:", overdue_count)
print("Total fines: Rs.", total_fine)

