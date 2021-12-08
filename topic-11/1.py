D = [
    (1, 5, 2, 3, 0, 4), # 'U'
    (3, 1, 0, 5, 4, 2), # 'R'
    (4, 0, 2, 3, 5, 1), # 'D'
    (2, 1, 5, 0, 4, 3), # 'L'
]
C = 'NESW'

*L, = map(int, input().split())
for c in input():
    L[:] = (L[e] for e in D[C.index(c)])
print(L[0])
