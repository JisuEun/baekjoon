import sys
input = sys.stdin.readline

N = int(input())

words = []

for _ in range(N):
    w = input().strip()
    words.append(w)

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)