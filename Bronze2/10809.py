S = input()

alphebet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [-1 for _ in range(26)]

# 알파벳별로 처음 등장하는거 순회 (이중 for문)
for i, a in enumerate(alphebet):
    for j, s in enumerate (S):
        if a == s and answer[i] == -1:
            answer[i] = j

print(*answer)