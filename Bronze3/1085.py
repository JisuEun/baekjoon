x, y, w, h = map(int, input().split())

# w-x, x, y-h, y 중 최솟값

print(min(abs(w-x), x, abs(y-h), y))