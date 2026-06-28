# Word Frequency Analysis

from collections import Counter

# Load text file
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Preprocessing
text = text.lower()
words = text.split()

# Frequency analysis
word_counts = Counter(words)

# Top 10 words
top_words = word_counts.most_common(10)

print("Top 10 words:")
for word, freq in top_words:
    print(word, ":", freq)

# Save results
with open("results.txt", "w", encoding="utf-8") as file:
    for word, freq in top_words:
        file.write(f"{word}: {freq}\n")
