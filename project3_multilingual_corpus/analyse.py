from collections import Counter
import re

def preprocess(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

def analyze(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    words = preprocess(text)
    return Counter(words)

korean = analyze("data/korean.txt")
french = analyze("data/french.txt")
english = analyze("data/english.txt")

print("Top Korean words:", korean.most_common(10))
print("Top French words:", french.most_common(10))
print("Top English words:", english.most_common(10))
