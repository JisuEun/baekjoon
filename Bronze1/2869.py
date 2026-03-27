A, B, V = map(int, input().split())

if (V-B)%(A-B) == 0:
    day = int((V-B)/(A-B))
else:
    day = int((V-B)/(A-B)) + 1

print(day)