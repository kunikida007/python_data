H, W = 1, 5
hash = [""] * (H+1)
for i in range(H+1):
    Y = 1,1,3,4,5
    hash[i] = Y
    W_sums = sum(hash[i])
    W_sums.append(hash[i])
    X = " ".join(hash[i])
    print(X)