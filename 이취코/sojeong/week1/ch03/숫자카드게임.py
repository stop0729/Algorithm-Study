# 숫자 카드 게임

# 행마다 가장 낮은 숫자 중 max값
N, M = map(int, input().split())
card = []

for i in range(N):
    row = list(map(int, input().split()))
    card.append(row)

result = max([min(c) for c in card])

print(result)