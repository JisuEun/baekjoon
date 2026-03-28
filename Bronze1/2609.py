A, B = map(int, input().split())

a, b = A, B

while b != 0:
    a, b = b, a%b

gcd = a
lcm = A*B // gcd

print(gcd)
print(lcm)