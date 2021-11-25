H, W = map(int, input().split())
list1 = []
for i in range(H):
    a = list(map(int, input().split()))
    list1.append(a)
for j in range(W):
    list2 = list(map(int, input().split()))
for x in range(H):
    sum = 0
    for y in range(W):
        sum += (list1[x][y] * list2[y])
    print(sum)
