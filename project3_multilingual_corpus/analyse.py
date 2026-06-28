from collections import Counter
import re

def preprocess(text):
    text = text.lower()
    return re.findall(r'\b\w+\b', text)

def analyze(file):
    with open(file, "r", encoding="utf-8") as f:
        return Counter(preprocess(f.read()))

languages = ["korean", "french", "english"]

results = {}

for lang in languages:
    results[lang] = analyze(f"data/{lang}.txt")

for lang, data in results.items():
    print(f"\n=== {lang.upper()} TOP WORDS ===")
    for word, freq in data.most_common(10):
        print(word, freq)
