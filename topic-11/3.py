D = [
    (1, 5, 2, 3, 0, 4), # 'U'
    (3, 1, 0, 5, 4, 2), # 'R'
    (4, 0, 2, 3, 5, 1), # 'D'
    (2, 1, 5, 0, 4, 3), # 'L'
]

*L1, = map(int, input().split())
*L2, = map(int, input().split())

p = (0, 0, 0, 1, 1, 2, 2, 3)*3
ok = 0
for k in p:
    if L1 == L2:
        ok = 1
    L2[:] = [L2[e] for e in D[k]]

print("Yes" if ok else "No")