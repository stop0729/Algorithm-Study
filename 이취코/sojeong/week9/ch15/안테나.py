# 안테나는 집이 있는 곳에만 설치할 수 있기 때문에 중앙값 이용

N = int(input()) # 집의 수 N

houses = list(map(int, input().split()))

houses.sort()

# 중앙값 O(1)
result = houses[(N-1)//2]
print(result)

# # 평균값 -> 틀림림
# result = sum(houses)//N
# print(result)