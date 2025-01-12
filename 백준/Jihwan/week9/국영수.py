N = int(input())
lst = []

for i in range(N):
    a, b, c, d = input().split()
    lst.append([a,b,c,d])

lst = sorted(lst, key = lambda x: x[1], reverse=True)

# for i in range(1, N):
#     if (lst[i][1] == lst[i-1][1] and lst[i][2] == lst[i-1][2] and lst[i][3] == lst[i-1][3] and lst[i][0] > lst[i-1][0]):
#         lst[i][0], lst[i-1][0] = lst[i-1][0], lst[i][0]
#     elif (lst[i][1] == lst[i-1][1] and lst[i][2] == lst[i-1][2] and lst[i][3] < lst[i-1][3]):
#         lst[i][3], lst[i-1][3] = lst[i-1][3], lst[i][3]
#     elif (lst[i][1] == lst[i-1][1] and lst[i][2] > lst[i-1][2]):
#         lst[i][2], lst[i-1][2] = lst[i-1][2], lst[i][2]
#         print('aaaaaaaaa')


lst = sorted(lst, key = lambda x: (-x[1], x[2], -x[3], x[4]))

for i in range(N):
    print(lst[i])