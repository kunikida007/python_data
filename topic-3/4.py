a, b, c = map(int, input().split())
hash = []
for i in range(a, b + 1):
    if c % i == 0:
        hash.append(c)
print(len(hash))
