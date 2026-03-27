ISBN = list(input().strip())

idx = -1
product = 0
sum = 0
for i in range(len(ISBN)):
    if ISBN[i] != "*":
        if i%2 == 0:
            ISBN[i] = int(ISBN[i])
        else:
            ISBN[i] = int(ISBN[i]) * 3
        sum += ISBN[i]
    else:
        idx = i
        if i%2 == 0:
            product = 1
        else:
            product = 3

for i in range(0, 10):
    if (i*product + sum)%10 == 0:
        ISBN[idx] = i

print(ISBN[idx])