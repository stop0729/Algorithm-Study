temp = input()
string = ['a','b','c','d','e','f','g','h']
x = int(temp[1])
y = string.index(temp[0]) + 1

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

result = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <1 or ny <1 or nx >8 or ny>8:
        continue
    result += 1

print(result)