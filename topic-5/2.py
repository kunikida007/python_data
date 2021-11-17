while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    i = 0
    print("#" * W)
    while i < H - 2:
        print("#", "." * (W-2), "#", sep="")
        i += 1
    print("#" * W)
    print()
