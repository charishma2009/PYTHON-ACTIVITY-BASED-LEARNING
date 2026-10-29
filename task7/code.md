

## 1. Problem Statement

Develop a Python program to analyze water distribution across multiple areas over several days. The program should compare the actual water supplied with the required demand, calculate shortages, measure the percentage of demand fulfilled, and identify the most underserved areas.

The program should:

- Accept water demand and actual supply for each area over several days.
- Calculate daily water shortages.
- Calculate total demand, total supply, and total shortage for each area.
- Calculate the percentage of demand fulfilled.
- Compare distribution levels across areas.
- Identify the most underserved area based on the lowest demand fulfillment percentage.

## 2. Algorithm

1. Start the program.
2. Input the number of areas and the number of days.
3. Enter the area name, daily water demand, and actual supply.
4. Validate that demand and supply values are non-negative.
5. Calculate daily shortages using `shortage = demand - supply` when demand exceeds supply; otherwise, shortage is zero.
6. Calculate total demand, total supply, and total shortage for each area.
7. Calculate the demand fulfillment percentage for each area.
8. Compare fulfillment percentages across areas.
9. Identify the area with the lowest fulfillment percentage.
10. Display the area-wise water distribution report.
11. Stop the program.

## 3. Flowchart 

```mermaid

flowchart TD
    A([Start]) --> B[Input areas and number of days]
    B --> C[Input daily demand and supply]
    C --> D{Are values non-negative?}
    D -- No --> E[Display invalid input]
    D -- Yes --> F[Calculate daily shortage]
    F --> G[Calculate area totals]
    G --> H[Calculate fulfillment percentage]
    H --> I{More areas or days?}
    I -- Yes --> C
    I -- No --> J[Compare area fulfillment]
    J --> K[Identify most underserved area]
    K --> L[Display report]
    L --> M([Stop])
    E --> M
```

## 4. Python Source Code

python

```

# Water Distribution Fairness Analysis

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
```

## 5. Sample Input

Assume all water quantities are measured in litres for simplicity.

text

```
Enter number of areas: 3
Enter number of days: 2

Enter name of area 1: North
Day 1 for North
Enter water demand: 1000
Enter actual supply: 800
Day 2 for North
Enter water demand: 1000
Enter actual supply: 700

Enter name of area 2: South
Day 1 for South
Enter water demand: 1000
Enter actual supply: 900
Day 2 for South
Enter water demand: 1000
Enter actual supply: 950

Enter name of area 3: East
Day 1 for East
Enter water demand: 1000
Enter actual supply: 600
Day 2 for East
Enter water demand: 1000
Enter actual supply: 500
```

## 6. Sample Output

text

```
===== WATER DISTRIBUTION REPORT =====

Area: East
Total demand: 2000.00
Total supply: 1100.00
Total shortage: 900.00
Demand fulfilled: 55.00%

Area: North
Total demand: 2000.00
Total supply: 1500.00
Total shortage: 500.00
Demand fulfilled: 75.00%

Area: South
Total demand: 2000.00
Total supply: 1850.00
Total shortage: 150.00
Demand fulfilled: 92.50%

Most underserved area: East
Fulfillment percentage: 55.00%
```

