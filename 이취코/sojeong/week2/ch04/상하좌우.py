# 상하좌우

N = int(input()) # 공간의 크기
move = [(0, -1), (0, 1), (-1, 0), (1, 0)] # L, R, U, D

x, y = 1,1 # 처음 자리
# R, R, R, U, D, D 입력 받기
plans = input().split()

for plan in plans:
    if plan == 'L':
        nx = x + move[0][0]
        ny = y + move[0][1]
    elif plan == 'R':   
        nx = x + move[1][0]
        ny = y + move[1][1]
    elif plan == 'U':
        nx = x + move[2][0]
        ny = y + move[2][1]
    elif plan == 'D':
        nx = x + move[3][0]
        ny = y + move[3][1]
        
    if nx < 1 or ny < 1 or nx > N or ny > N: # 공간을 벗어나면 무시
        continue
    
    x, y = nx, ny

print(x, y)
  
# 입력        
# 5
# R R R U D D 
# 출력 3, 4