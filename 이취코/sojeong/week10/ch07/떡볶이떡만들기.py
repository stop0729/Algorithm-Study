# 떡볶이 떡 만들기

N, M = map(int, input().split())
rice_cakes = list(map(int, input().split()))

rice_cakes.sort() # 10 15 17 19
start = 0
end = max(rice_cakes)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for rice_cake in array:
            if rice_cake > mid:
                total += rice_cake - mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(binary_search(rice_cakes, M, start, end))

'''
4 6
19 15 10 17
'''