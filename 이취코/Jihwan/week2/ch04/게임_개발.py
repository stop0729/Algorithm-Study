n, m = map(int, input().split())
x, y, d = map(int, input().split())

place = []
for i in range(n):
    place.append(list(map(int, input().split())))

place[x][y] = -1

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1] # 북:0, 동:1, 남:2, 서:3 순서

def cal_d(temp, dir):
    temp += dir
    if temp < 0:
        temp += 4
    return temp

result = 1

while True:
    is_move = False

    for _ in range(4):
        d = cal_d(d, -1)
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < n and nx >=0 and ny <n and ny >=0 and place[nx][ny] == 0:
            x, y = nx, ny
            place[nx][ny] = -1
            is_move = True
            break

    if is_move:
        result += 1
        continue
    else:
        d_c = cal_d(d, -2)
        nx = x + dx[d_c]
        ny = y + dy[d_c]
        if nx <n and ny >=0 and ny <n and ny >=0 and place[nx][ny] != 1:
            x, y = nx, ny
        else:
            break

    
print(result)