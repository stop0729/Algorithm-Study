# 1,2,3 더하기
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

T = int(input())
N = list(map(int, [input() for _ in range(T)]))

d = [0] * 11

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]
    
for n in N:
    print(d[n])
    