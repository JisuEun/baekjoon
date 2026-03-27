H, M = map(int, input().split())

if M < 45:
    if H == 0:
        H_alarm = 23
    else:
        H_alarm = H - 1
    M_alarm = M + 15
else:
    H_alarm = H
    M_alarm = M - 45

print(H_alarm, M_alarm)