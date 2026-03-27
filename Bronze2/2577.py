A = int(input())
B = int(input())
C = int(input())

calc = A*B*C
dict = {}
for i in range(0, 10):
    dict[i] = 0

for x in str(calc):
    dict[int(x)] += 1

for i in range(0, 10):
    print(dict[i])