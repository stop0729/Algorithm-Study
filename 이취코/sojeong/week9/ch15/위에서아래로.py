# 위에서 아래로

N = int(input())
array = [int(input()) for _ in range(N)]

array.sort(reverse=True)

for i in array:
    print(i, end=' ')