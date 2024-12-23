# 성적이 낮은 순서로 학생 출력하기

N = int(input())
dic = {}

for i in range(N):
    name, score = input().split()
    dic[name] = int(score)
    
result = sorted(dic.items(), key = lambda x: x[1])

for  r in result:
    print(r[0], end=' ')
