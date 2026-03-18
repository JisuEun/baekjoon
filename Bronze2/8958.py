import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    grade = input()
    cnt = 0
    score = 0
    for idx, g in enumerate(grade):
        if g == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)