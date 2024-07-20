def string_matching(pattern: str, text: str):
    m = len(pattern)
    n = len(text)
    for i in range(n-m+1):
        j=0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index: {i}")

if __name__ == '__main__':
    text = input("Enter text: ")
    print(text)
    pattern = input("Enter pattern: ")
    print(pattern)
    string_matching(pattern, text)