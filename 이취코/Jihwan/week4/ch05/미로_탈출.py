from collections import deque

N, M = map(int, input().split())

miro = []

for i in range(N):
    temp = input()
    miro.append([])
    for j in range(M):
        miro[i].append(int(temp[j]))

distance = [[999999]*M for i in range(N)]
start = [0,0]
print(miro)

distance[start[0]][start[1]] = 0
queue = deque([start])

while queue:

    current = queue.popleft()
    if current[0] + 1 < N:
        if miro[current[0]+1][current[1]] == 1 and distance[current[0]+1][current[1]] > distance[current[0]][current[1]] + 1:
            queue.append([current[0]+1, current[1]])
            distance[current[0]+1][current[1]] = distance[current[0]][current[1]] + 1

    if current[1] + 1 < M:
        if miro[current[0]][current[1]+1] == 1 and distance[current[0]][current[1]+1] > distance[current[0]][current[1]] + 1:
            queue.append([current[0], current[1]+1])
            distance[current[0]][current[1]+1] = distance[current[0]][current[1]] + 1

    if current[0] - 1 > -1: 
        if miro[current[0]-1][current[1]] == 1 and distance[current[0]-1][current[1]] > distance[current[0]][current[1]] + 1:
            queue.append([current[0]-1, current[1]])
            distance[current[0]-1][current[1]] = distance[current[0]][current[1]] + 1

    if current[1] - 1 > -1:
        if miro[current[0]][current[1]-1] == 1 and distance[current[0]][current[1]-1] > distance[current[0]][current[1]] + 1:
            queue.append([current[0], current[1]-1])
            distance[current[0]][current[1]-1] = distance[current[0]][current[1]] + 1

print(distance)
print(distance[N-1][M-1]+1)