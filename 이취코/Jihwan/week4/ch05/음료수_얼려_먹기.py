N, M = map(int, input().split())

def dfs(graph, j, k):
    if graph[j][k] == 0:
        graph[j][k] = 1
        if j+1 < N:
            dfs(graph, j+1, k)
        if k+1 < M:
            dfs(graph, j, k+1)
        if j-1 > -1:
            dfs(graph, j-1, k)
        if k-1 > -1:
            dfs(graph, j, k-1)


        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]


    
ice = []
for i in range(N):
    temp = input()
    ice.append([])
    for k in range(M):
        ice[i].append(int(temp[k]))
        

result = 0

for i in range(N):          
    for j in range(M):
        if ice[i][j] == 0:
            result += 1
            dfs(ice, i, j)

print(result)

"""
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
"""
