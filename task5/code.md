## Progressive Electricity Billing System


## 1. Problem Statement

Progressive Electricity Billing: Calculate household bills using multiple consumption slabs, fixed charges, surcharges, and rebates, then compare bills across several months and identify unusual increases

## 2. Algorithm

1. Start the program.
2. Input the number of months.
3. For each month, input the electricity consumption in units.
4. Calculate the energy charge using progressive slabs.
5. Add the fixed monthly charge.
6. Apply the surcharge or rebate according to the consumption.
7. Calculate and store the final bill.
8. Compare the bill with the previous month's bill.
9. If the increase exceeds 30%, display an unusual-increase warning.
10. Display the monthly billing report.
11. Stop the program.

## 3. Flowchart 

```mermaid

flowchart TD
    A([Start]) --> B[Input number of months]
    B --> C[Input monthly consumption]
    C --> D[Calculate progressive energy charge]
    D --> E[Add fixed charge]
    E --> F{Units above 200?}
    F -- Yes --> G[Apply surcharge]
    F -- No --> H{Units at most 100?}
    H -- Yes --> I[Apply rebate]
    H -- No --> J[No adjustment]
    G --> K[Calculate final bill]
    I --> K
    J --> K
    K --> L{Previous month available?}
    L -- Yes --> M[Calculate percentage change]
    M --> N{Increase above 30 percent?}
    N -- Yes --> O[Display unusual increase warning]
    N -- No --> P[Store bill]
    O --> P
    L -- No --> P
    P --> Q{More months?}
    Q -- Yes --> C
    Q -- No --> R[Display billing report]
    R --> S([Stop])
```


## 5. Sample Input



```
Enter number of months: 3

Month 1
Enter units consumed: 80

Month 2
Enter units consumed: 120

Month 3
Enter units consumed: 250
```

## 6. Sample Output



```
===== ELECTRICITY BILL REPORT =====

Month 1
Units consumed: 80.00
Energy charge: Rs. 160.00
Fixed charge: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 8.00
Final bill: Rs. 252.00

Month 2
Units consumed: 120.00
Energy charge: Rs. 260.00
Fixed charge: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 0.00
Final bill: Rs. 360.00
Monthly change: 42.86%
Warning: Unusual bill increase!

Month 3
Units consumed: 250.00
Energy charge: Rs. 750.00
Fixed charge: Rs. 100.00
Surcharge: Rs. 37.50
Rebate: Rs. 0.00
Final bill: Rs. 887.50
Monthly change: 146.53%
Warning: Unusual bill increase!
```

 them with the applicable electricity provider's rules when using the program for actual billing.
