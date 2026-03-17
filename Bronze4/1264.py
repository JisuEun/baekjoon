import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    S = input().strip().lower()

    if S == "#":
        break

    for s in S:
        if s in vowel:
            cnt += 1

    print(cnt)