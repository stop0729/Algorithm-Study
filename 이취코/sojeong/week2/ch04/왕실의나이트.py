# 왕실의 나이트
# 8x8 체스판 

now = input()

# a1을 입력받으면 
x = int(now[1]) # 1 
y = int(ord(now[0]) - ord('a') + 1) # a
# ord : 문자의 아스키 코드 값

movements = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
count = 0

for move in  movements:
    nx = x + move[0] # x부분 
    ny = y + move[1] # y부분
    
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        count += 1

print(count) # 2