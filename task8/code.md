## Repeated Word and Phrase Detection Using Python

## 1. Problem Statement
Repeated Word and Phrase Detection: Process a paragraph, normalize letter case, count word occurrences using permitted string and list operations, and identify repeated words and their positions


## 2. Algorithm

1. Start the program.
2. Read a paragraph from the user.
3. Convert the entire paragraph into lowercase using `lower()`.
4. Remove punctuation using string operations.
5. Split the paragraph into individual words using `split()`.
6. Create an empty list to store unique words.
7. Traverse each word in the word list.
8. Count each word's occurrences using the `count()` function.
9. If the count is greater than one, identify it as a repeated word.
10. Find and display the positions of repeated words using list operations.
11. Generate consecutive two-word phrases.
12. Count phrase occurrences and identify repeated phrases.
13. Display the repeated words, their counts, positions, and repeated phrases.
14. Stop the program.

## 3. Flowchart 



```mermaid

flowchart TD
    A([Start]) --> B[/Enter a paragraph/]
    B --> C[Convert paragraph to lowercase]
    C --> D[Remove punctuation]
    D --> E[Split paragraph into words]
    E --> F[Initialize empty unique word list]
    F --> G{More words?}
    G -- Yes --> H[Get next word]
    H --> I{Word already in unique list?}
    I -- No --> J[Add word to unique list]
    I -- Yes --> G
    J --> G
    G -- No --> K[Count occurrences of each word]
    K --> L{Count greater than 1?}
    L -- Yes --> M[Find and display word positions]
    L -- No --> N[Check next word]
    M --> N
    N --> O[Generate consecutive two-word phrases]
    O --> P[Count repeated phrases]
    P --> Q[Display repeated words and phrases]
    Q --> R([Stop])
```


## 5. Sample Input



```
Enter a paragraph:

Python is easy to learn. Python is powerful.
Learning Python is easy and learning Python is fun.
```

## 6. Sample Output



```
--- REPEATED WORDS ---

Word: python
Occurrences: 4
Positions: [1, 5, 9, 13]

Word: is
Occurrences: 4
Positions: [2, 6, 10, 14]

Word: easy
Occurrences: 2
Positions: [3, 11]

Word: to
Occurrences: 1

Word: learn
Occurrences: 1

Word: powerful
Occurrences: 1

Word: learning
Occurrences: 2
Positions: [8, 12]

--- REPEATED PHRASES ---

No repeated phrases found.
```



