n = int(input())
x , y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'D', 'U']

for plan in plans:
    for i in range(len(move_types)): # i로 찾는 이유는 dx, dy index 정하기 위해서
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx > n or nx < 1 or ny <1 or ny > n:
        continue
    x , y = nx, ny

print(x, y)