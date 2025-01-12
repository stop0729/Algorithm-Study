n = int(input())
score = {}

for i in range(n):
    a, b = input().split()
    score[a] = b

# print(score)
# score = sorted(score)

# for i in range(n):
#     print(score[i], end = " ")



score = sorted(score.items(), key = lambda student : student[1])
for i in range(n):
    print(score[i][0], end = " ")