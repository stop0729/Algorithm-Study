# 시각
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

# 100만개 이하일 때 완전 탐색
N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                

print(count)
# 입력 5
# 출력 11475

# if 3 in [i, j, k]: # 33은 포함이 안됨
#     count += 1
