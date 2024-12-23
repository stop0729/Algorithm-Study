# 안테나

N = int(input()) # 집의 수 N

houses = list(map(int, input().split()))

antenas = list(range(min(houses), max(houses)+1))

#antena[j]-house[i]가 최소가 되도록.

min = 200000
for antena in antenas:
    sum = 0
    for house in houses:
        sum += abs(antena - house)
        
    if sum < min :
        min = sum      
        result = antena
        
print(result)