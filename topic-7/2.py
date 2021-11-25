while True:
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    ans = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            c = X-(a+b)
            if c > b and c <= N:
                ans += 1
    print("%d" % (ans))
