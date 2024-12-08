n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))


cnt_0 = 0
cnt_1 = 0
cnt_2 = 0

def check(row, col, n):
    global cnt_0, cnt_1, cnt_2
    current = paper[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if current != paper[i][j]:
                next_n = n//3
                for k in range(3):
                    for j in range(3):
                        check(row+(next_n*k), col+(next_n*j), next_n)
                        
                return
    
    if current == 0:
        cnt_0 += 1
    elif current == 1:
        cnt_1 += 1
    else:
        cnt_2 += 1

    return

check(0, 0, n)

print(cnt_2)
print(cnt_0)
print(cnt_1)

# global count = 

# def check1(N):
#     if n%3 >= 1:
#         return True
#     else:
#         return False
    
# def check2(paper):
#     temp = paper[0][0]
#     for i in range(len(paper)):
#         for j in range(len(paper)):
#             if temp == paper[i][j]:
#                 return True
#             else:
#                 return False
    
# number = {'-1':0, '1':0, '0':0}

# def cut(paper):
#     if check1(n):
#         if check2(paper):
#             if paper[0][0]

#         q = n%3
#         if paper[0][0]:
#             pass