S = input()

cnt0 = 0
cnt1 = 0

i = 0
while i < len(S):
    if S[i] == '0':
        cnt0 += 1
        while i < len(S) and S[i] == '0':
            i += 1
    else:
        cnt1 += 1
        while i < len(S) and S[i] == '1':
            i += 1

print(min(cnt0, cnt1))