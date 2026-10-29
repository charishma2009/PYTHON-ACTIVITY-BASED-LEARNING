

## 1. Problem Statement

Develop a Python program to manage library borrowing records using tuples containing book identifiers, borrowing periods, and return delays.

The program should calculate fines for overdue books, identify overdue records, and reconcile book availability by determining whether each book has been returned.

Rules used in this program:

- Each book has a unique book ID.
- The standard borrowing period is 14 days.
- The fine is ₹5 per overdue day.
- If the return delay is zero, the book is considered returned on time.
- If the return delay is greater than zero, the book is overdue.
- A book is available only if it has been returned.

## 2. Algorithm

1. Start the program.
2. Input the number of borrowing records.
3. For each record, input the book ID, borrowing period, return delay, and return status.
4. Store the information in tuples.
5. Calculate the overdue days using the return delay.
6. Calculate the fine as overdue days multiplied by ₹5.
7. Identify overdue books.
8. Determine availability based on the return status.
9. Display the fine, overdue status, and availability of each book.
10. Calculate and display the total fine.
11. Stop the program.

## 3. Flowchart 

'''mermaid

flowchart TD
    A([Start]) --> B[Input borrowing records]
    B --> C[Store records as tuples]
    C --> D[Read next book record]
    D --> E{Return delay greater than zero?}
    E -- Yes --> F[Calculate fine]
    E -- No --> G[Fine equals zero]
    F --> H{Book returned?}
    G --> H
    H -- Yes --> I[Mark book available]
    H -- No --> J[Mark book unavailable]
    I --> K[Display record]
    J --> K
    K --> L{More records?}
    L -- Yes --> D
    L -- No --> M[Calculate total fines]
    M --> N[Display summary]
    N --> O([Stop])
    '''

## 4. Simple Python Source Code

python

```

# Library Borrowing and Fine Reconciliation

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
```

## 5. Sample Input

text

```
Enter number of borrowing records: 3

Record 1
Enter book ID: B101
Enter borrowing period in days: 14
Enter return delay in days: 0
Has the book been returned? (yes/no): yes

Record 2
Enter book ID: B102
Enter borrowing period in days: 14
Enter return delay in days: 3
Has the book been returned? (yes/no): yes

Record 3
Enter book ID: B103
Enter borrowing period in days: 14
Enter return delay in days: 5
Has the book been returned? (yes/no): no
```

## 6. Sample Output

text

```
===== LIBRARY RECONCILIATION REPORT =====

Book ID: B101
Borrowing period: 14 days
Return delay: 0 days
Fine: Rs. 0
Status: On time
Availability: Available

Book ID: B102
Borrowing period: 14 days
Return delay: 3 days
Fine: Rs. 15
Status: Overdue
Availability: Available

Book ID: B103
Borrowing period: 14 days
Return delay: 5 days
Fine: Rs. 25
Status: Overdue
Availability: Not available

===== SUMMARY =====
Total records: 3
Overdue records: 2
Total fines: Rs. 40
```

