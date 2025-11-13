import re
from collections import Counter

with open("Захар Беркут.txt", "r") as f:
    text = f.read().lower()

text = re.sub(r"[^а-щьюяєіїґ\s]", " ", text)
words = text.split()

words = [w for w in words if len(w) >= 3]

word_freq = Counter(words)

pairs = []
for word in words:
    for i in range(len(word) - 1):
        pair = word[i:i+2]
        pairs.append(pair)

pair_freq = Counter(pairs)

least_100_words = word_freq.most_common()[:-101:-1]

least_50_pairs = pair_freq.most_common()[:-51:-1]

print("100 найрідкісніших слів:")
for w, c in least_100_words:
    print(f"{w} → {c}")

print("\n50 найрідкісніших пар літер:")
for p, c in least_50_pairs:
    print(f"{p} → {c}")
