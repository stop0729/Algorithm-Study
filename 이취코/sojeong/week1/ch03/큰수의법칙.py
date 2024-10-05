# 큰 수의 법칙

# 주어진 수들을 M번 더하여 가장 큰 수를 만든다
# 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

# 입력
N, M, K = map(int, input().split())
num = list(map(int, input().split()))

# 내림차순
num.sort(reverse=True)

sum = 0
# 첫번째꺼 K번 더한다
# 두번째꺼 1번 더한다
# 첫번째꺼 K번 더한다
# ...

while M > 0:
    sum += (num[0]*K + num[1]*(int(M!=0)))
    M -= (K + int(M!=0))

print(sum)