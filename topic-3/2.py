list1 = []
while True:
    N = int(input())
    if N == 0:
        break
    list1.append(N)
for i, j in enumerate(list1):
    print("Case ", i + 1, ":", " ", j, sep="")
