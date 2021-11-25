cnt = [0]*120
n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    v = (a - 1) * 30 + (b - 1) * 10 + (c - 1)
    cnt[v] += d
for i in range(4):
    for j in range(3):
        s = ""
        for k in range(10):
            s += " " + str(cnt[i * 30 + j * 10 + k])
        print(s)
    if i <= 2:
        print("####################")
