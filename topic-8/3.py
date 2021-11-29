import sys
s = [x.lower() for x in sys.stdin.read().split()]
words = "".join(s)
alfa = "abcdefghijklmnopqrstuvwxyz"
hash = {}
for i in alfa:
    hash[i] = 0
for j in words:
    if j in hash:
        hash[j] += 1
for k, v in hash.items():
    print(k, ":", v)
