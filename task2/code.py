
subjects = input("Enter subject names separated by spaces: ").split()
n = int(input("Enter number of examinations: "))

if not subjects or n < 2:
    print("Enter at least one subject and two examinations.")
else:
    marks = {}

    for subject in subjects:
        marks[subject] = []
        for i in range(n):
            score = float(input(
                f"Enter marks in {subject} for Exam {i + 1}: "
            ))
            if score < 0 or score > 100:
                print("Invalid marks! Enter values from 0 to 100.")
                raise SystemExit
            marks[subject].append(score)

    # Calculate examination averages
    averages = []
    for i in range(n):
        avg = sum(marks[s][i] for s in subjects) / len(subjects)
        averages.append(avg)

    print("\nEXAMINATION AVERAGES")
    for i, avg in enumerate(averages):
        print(f"Exam {i + 1}: {avg:.2f}")

    # Compare examination trends
    print("\nPERFORMANCE TRENDS")
    for i in range(1, n):
        change = averages[i] - averages[i - 1]
        if change > 0:
            print(f"Exam {i} to Exam {i + 1}: Improved by {change:.2f}")
        elif change < 0:
            print(f"Exam {i} to Exam {i + 1}: Declined by {abs(change):.2f}")
        else:
            print(f"Exam {i} to Exam {i + 1}: No change")

    # Identify consistently weak subjects
    weak = [
        s for s in subjects
        if all(score < 40 for score in marks[s])
    ]

    print("\nCONSISTENTLY WEAK SUBJECTS")
    print(", ".join(weak) if weak else "None")

    # Calculate overall average and classify
    overall = sum(averages) / n

    if overall >= 80:
        category = "Excellent"
    elif overall >= 60:
        category = "Good"
    elif overall >= 40:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(f"\nOverall Average: {overall:.2f}")
    print(f"Student Classification: {category}")

