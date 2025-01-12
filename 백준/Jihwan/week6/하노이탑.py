n = int(input())
result = 0

def move(a, b, n):
    if n == 1:
        print(a, b) # 1~3을 움직인다고 하면 1을 움직일때

        return 0
    move(a, 6-a-b, n-1) # (2, 1, 1) b=3, a= 2
    print(a, b) # 1~3을 움직인다고 하면 3을 움직일때
    move(6-a-b, b, n-1) # (2, 3, 2)
    return 0

move(1, 3, n) 