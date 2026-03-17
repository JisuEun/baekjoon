import sys
input = sys.stdin.readline

while True:
    name, age, weight = input().split()
    if name == "#":
        break
    age = int(age)
    weight = int(weight)

    print(f"{name} Senior" if age > 17 or weight >= 80 else f"{name} Junior")