# Sentence Length Analysis

import re

def sentence_lengths(text):
    sentences = re.split(r'[.!?]', text)
    lengths = []

    for sentence in sentences:
        words = sentence.split()
        if len(words) > 0:
            lengths.append(len(words))

    return lengths

# Load texts
with open("text1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("text2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

# Analysis
len1 = sentence_lengths(text1)
len2 = sentence_lengths(text2)

print("Text 1 average sentence length:", sum(len1)/len(len1))
print("Text 2 average sentence length:", sum(len2)/len(len2))
