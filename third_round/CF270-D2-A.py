for _ in range(int(input())):
    angle = int(input())
    print("YES" if 360 % (180 - angle) == 0 else "NO")
