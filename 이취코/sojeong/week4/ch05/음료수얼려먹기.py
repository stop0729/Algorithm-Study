# 음료수 얼려 먹기
N, M = map(int, input().split())

ice = []
for i in range(N):
    ice.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False # 종료조건
    if ice[x][y] == 0: # 방문하지 않은 노드라면
        ice[x][y] = 1 # 방문 처리

        # 연결된 지점 방문
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False 

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

'''

# 8