import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == "#":
        break
    cnt = 0
    for s in S.lower():
        if s in "aeiou":
            cnt += 1
    print(cnt)