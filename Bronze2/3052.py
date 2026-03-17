arr = [int(input()) for _ in range(10)]
arr = [x%42 for x in arr]
print(len(set(arr)))