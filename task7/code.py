
areas = int(input("Enter number of areas: "))
days = int(input("Enter number of days: "))

if areas <= 0 or days <= 0:
    print("Invalid number of areas or days")
    raise SystemExit

records = []

for i in range(areas):
    name = input(f"\nEnter name of area {i + 1}: ")

    total_demand = 0
    total_supply = 0
    total_shortage = 0

    for day in range(days):
        print(f"Day {day + 1} for {name}")
        demand = float(input("Enter water demand: "))
        supply = float(input("Enter actual supply: "))

        if demand < 0 or supply < 0:
            print("Demand and supply must be non-negative")
            raise SystemExit

        shortage = max(0, demand - supply)

        total_demand += demand
        total_supply += supply
        total_shortage += shortage

    if total_demand > 0:
        fulfillment = min(100, total_supply / total_demand * 100)
    else:
        fulfillment = 100

    records.append((
        name, total_demand, total_supply,
        total_shortage, fulfillment
    ))

# Sort areas by fulfillment percentage
records.sort(key=lambda x: x[4])

print("\n===== WATER DISTRIBUTION REPORT =====")

for name, demand, supply, shortage, fulfillment in records:
    print(f"\nArea: {name}")
    print(f"Total demand: {demand:.2f}")
    print(f"Total supply: {supply:.2f}")
    print(f"Total shortage: {shortage:.2f}")
    print(f"Demand fulfilled: {fulfillment:.2f}%")

print("\nMost underserved area:", records[0][0])
print("Fulfillment percentage:", f"{records[0][4]:.2f}%")

