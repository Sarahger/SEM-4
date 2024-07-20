import re
from collections import Counter

def count_word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)
    return word_freq

def generate_report(word_freq, n=5):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {n} most frequently occurring words:")
    for word, freq in sorted_word_freq[:n]:
        print(f"{word}: {freq} times")

def first_word(text):
    words = re.findall(r'\b\w+\b', text)
    if words:
        print("Keyword :", words[0])

def main():
    file = open('EXP6/sample_text.txt', 'r')
    text = file.read()
    word_freq = count_word_frequency(text)
    generate_report(word_freq)
    first_word(text)

if __name__ == "__main__":
    main()
