while True:
    m, f, r = 20, 30, -1
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        print("F")
    elif m + f >= 80:
        print("A")
    elif 80 > m + f >= 65:
        print("B")
    elif 65 > m + f >= 50:
        print("C")
    elif 50 > m + f >= 30:
        if r >= 50:
            print("C")
        else:
            print("D")
    elif 30 > m + f:
        print("F")
