height = [int(input()) for _ in range(9)]

_sum = sum(height) - 100
tmp1 = tmp2 = -1
for i in range(9):
    for j in range(i+1, 9):
        if height[i] + height[j] == _sum:
            tmp1 = i
            tmp2 = j

height.pop(tmp1)
height.pop(tmp2-1)
height.sort()

for h in height:
    print(h)