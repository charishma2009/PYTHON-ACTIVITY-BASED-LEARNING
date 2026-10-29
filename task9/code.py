

items = input("Enter supply names separated by spaces: ").split()
stock = []

for item in items:
    quantity = int(input(f"Available stock of {item}: "))
    stock.append(quantity)

n = int(input("Enter number of affected areas: "))
areas = []

for i in range(n):
    print(f"\nArea {i + 1}")
    name = input("Area name: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority")
        raise SystemExit

    requirements = []

    for item in items:
        quantity = int(input(f"{item} required: "))
        if quantity < 0:
            print("Invalid requirement")
            raise SystemExit
        requirements.append(quantity)

    areas.append((name, priority, requirements))

# High priority areas are processed first
priority_order = {"High": 1, "Medium": 2, "Low": 3}
areas.sort(key=lambda area: priority_order[area[1]])

unmet_total = [0] * len(items)

print("\n===== RELIEF ALLOCATION REPORT =====")

for name, priority, requirements in areas:
    print(f"\nArea: {name} | Priority: {priority}")

    for i in range(len(items)):
        allocated = min(stock[i], requirements[i])
        unmet = requirements[i] - allocated

        stock[i] -= allocated
        unmet_total[i] += unmet

        print(
            f"{items[i]}: Required={requirements[i]}, "
            f"Allocated={allocated}, Unmet={unmet}"
        )

print("\n===== REMAINING STOCK =====")

for i in range(len(items)):
    print(items[i], ":", stock[i])

print("\n===== TOTAL UNMET DEMAND =====")

for i in range(len(items)):
    print(items[i], ":", unmet_total[i])

