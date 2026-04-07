dic_h = {}
dic_v = {}

for _ in range(3):
    a, b = map(int, input().split())
    dic_h[a] = dic_h.get(a, 0) + 1
    dic_v[b] = dic_v.get(b, 0) + 1

x = y = 0
for h in dic_h:
    if dic_h[h] == 1:
        x = h

for v in dic_v:
    if dic_v[v] == 1:
        y = v

print(x, y)