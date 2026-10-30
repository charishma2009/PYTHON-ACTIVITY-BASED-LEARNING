
# Repeated Word and Phrase Detection

# Step 1: Get paragraph from user
paragraph = input("Enter a paragraph: ")

# Step 2: Convert to lowercase
paragraph = paragraph.lower()

# Step 3: Remove punctuation
for symbol in ".,!?;:\"'()[]{}":
    paragraph = paragraph.replace(symbol, "")

# Step 4: Split paragraph into words
words = paragraph.split()

# Step 5: Find unique words
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Step 6: Detect repeated words
print("\n--- REPEATED WORDS ---")

found = False

for word in unique_words:
    count = words.count(word)

    if count > 1:
        found = True

        # Find positions (1-based indexing)
        positions = []

        for i in range(len(words)):
            if words[i] == word:
                positions.append(i + 1)

        print("Word:", word)
        print("Occurrences:", count)
        print("Positions:", positions)

if not found:
    print("No repeated words found.")

# Step 7: Generate consecutive two-word phrases
phrases = []

for i in range(len(words) - 1):
    phrase = words[i] + " " + words[i + 1]
    phrases.append(phrase)

# Step 8: Find unique phrases
unique_phrases = []

for phrase in phrases:
    if phrase not in unique_phrases:
        unique_phrases.append(phrase)

# Step 9: Detect repeated phrases
print("\n--- REPEATED PHRASES ---")

phrase_found = False

for phrase in unique_phrases:
    count = phrases.count(phrase)

    if count > 1:
        phrase_found = True

        positions = []

        for i in range(len(phrases)):
            if phrases[i] == phrase:
                positions.append(i + 1)

        print("Phrase:", phrase)
        print("Occurrences:", count)
        print("Positions:", positions)

if not phrase_found:
    print("No repeated phrases found.")


