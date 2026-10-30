# Multi-Route Courier Dispatch Planning Using Python

## 1. Problem Statement
Multi-Route Courier Dispatch Planning: Process package weights, destination zones, vehicle capacities, and delivery priorities; allocate packages to vehicles and identify packages that cannot be dispatched


## 2. Algorithm

1. Start the program.
2. Input the number of packages and vehicles.
3. For each package, input its ID, weight, destination zone, and priority.
4. For each vehicle, input its ID, maximum capacity, and destination zone.
5. Sort packages by priority: High, Medium, then Low.
6. For each package:
   - Search for a vehicle serving the same destination zone.
   - Check whether the vehicle has enough remaining capacity.
   - If a suitable vehicle is available, allocate the package and update the remaining capacity.
   - Otherwise, mark the package as undispatched.
7. Display the packages allocated to each vehicle and its remaining capacity.
8. Display the list of undispatched packages.
9. Stop the program.

## 3.  Flowchart 
```mermaid

flowchart TD
    A([Start]) --> B[Input packages and vehicles]
    B --> C[Sort packages by priority]
    C --> D[Select next package]
    D --> E{Matching zone vehicle available?}
    E -- No --> H[Mark package undispatched]
    E -- Yes --> F{Capacity sufficient?}
    F -- Yes --> G[Allocate package and update capacity]
    F -- No --> H
    G --> I{More packages?}
    H --> I
    I -- Yes --> D
    I -- No --> J[Display dispatch summary]
    J --> K([Stop])
```


## 5. Sample Input



```
Enter number of packages: 5

Package 1
Package ID: P101
Weight (kg): 10
Destination zone: A
Priority (High/Medium/Low): High

Package 2
Package ID: P102
Weight (kg): 15
Destination zone: A
Priority (High/Medium/Low): Medium

Package 3
Package ID: P103
Weight (kg): 20
Destination zone: B
Priority (High/Medium/Low): High

Package 4
Package ID: P104
Weight (kg): 25
Destination zone: A
Priority (High/Medium/Low): Low

Package 5
Package ID: P105
Weight (kg): 40
Destination zone: B
Priority (High/Medium/Low): Medium

Enter number of vehicles: 2

Vehicle 1
Vehicle ID: V1
Capacity (kg): 30
Destination zone: A

Vehicle 2
Vehicle ID: V2
Capacity (kg): 50
Destination zone: B
```

## 6. Sample Output



```
===== COURIER DISPATCH REPORT =====

Vehicle: V1
Destination Zone: A
Packages: P101, P102
Remaining Capacity: 5.00 kg

Vehicle: V2
Destination Zone: B
Packages: P103, P105
Remaining Capacity: -10.00 kg

Undispatched Packages: P104
```

Correction to the sample output: Vehicle V2 has a capacity of 50 kg, and packages P103 and P105 weigh 20 kg and 40 kg. Their combined weight is 60 kg, so both cannot be allocated to V2. The correct output is:

text

```
===== COURIER DISPATCH REPORT =====

Vehicle: V1
Destination Zone: A
Packages: P101, P102
Remaining Capacity: 5.00 kg

Vehicle: V2
Destination Zone: B
Packages: P103
Remaining Capacity: 30.00 kg

Undispatched Packages: P104, P105
```

