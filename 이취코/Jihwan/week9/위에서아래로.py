n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

result = sorted(lst, reverse=True)

for i in range(n):
    print(result[i], end = ' ')    