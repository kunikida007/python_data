W, H, x, y, r = map(int, input().split())
print("Yes"*(r <= x <= W-r) * (r <= y <= H-r) or "No")
