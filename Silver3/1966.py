from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    cnt = 0
    while True:
        while queue[0] < max(queue):
            queue.append(queue.popleft())
            if M == 0:
                M = N - 1
            else:
                M -= 1

        if M == 0 and queue[0] == max(queue):
            print(cnt + 1)
            break

        queue.popleft()
        N -= 1
        cnt += 1
        if M == 0:
            M = N - 1
        else:
            M -= 1

        if len(queue) == 0:
            print(N)
            break
