

MIN_AGGREGATE = 75
MIN_SUBJECT = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

applicants = []
eligible = []
rejected = []

n = int(input("Enter number of applicants: "))
subjects = int(input("Enter number of subjects: "))

if n <= 0 or subjects <= 0:
    print("Invalid number of applicants or subjects")
    raise SystemExit

for i in range(n):
    print("\nApplicant", i + 1)

    aid = input("Applicant ID: ")
    name = input("Name: ")

    marks = []
    for j in range(subjects):
        score = float(input(f"Subject {j + 1} marks: "))
        if score < 0 or score > 100:
            print("Invalid marks")
            raise SystemExit
        marks.append(score)

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))

    if not 0 <= attendance <= 100 or income < 0:
        print("Invalid attendance or income")
        raise SystemExit

    aggregate = sum(marks) / subjects
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if min(marks) < MIN_SUBJECT:
        reasons.append("Subject mark below 60%")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Income exceeds Rs. 250000")

    applicant = (
        aid, name, aggregate, attendance, income
    )

    if len(reasons) == 0:
        eligible.append(applicant)
    else:
        rejected.append((aid, name, reasons))

# Ranking:
# 1. Higher aggregate
# 2. Higher attendance
# 3. Lower income
# 4. Alphabetical applicant ID
eligible.sort(
    key=lambda x: (-x[2], -x[3], x[4], x[0].lower())
)

print("\n===== ELIGIBLE SCHOLARSHIP APPLICANTS =====")

if not eligible:
    print("No eligible applicants")
else:
    print("Rank | ID | Name | Aggregate | Attendance | Income")

    for rank, applicant in enumerate(eligible, start=1):
        aid, name, aggregate, attendance, income = applicant

        print(
            rank, "|", aid, "|", name, "|",
            f"{aggregate:.2f}%", "|",
            f"{attendance:.2f}%", "|",
            f"Rs. {income:.2f}"
        )

print("\n===== REJECTED APPLICANTS =====")

if not rejected:
    print("No rejected applicants")
else:
    for aid, name, reasons in rejected:
        print(aid, "|", name, "|", ", ".join(reasons))

