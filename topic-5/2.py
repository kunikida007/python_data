while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        if i == H-1 or i == 0:
            print("#" * W)
        else:
            print("#", "." * (W-2), "#", sep="")
