# 부품 찾기

N = int(input())
parts = list(map(int, input().split()))
M = int(input())
requests = list(map(int, input().split()))      

# 먼저 정렬
parts.sort() # 2 3 7 8 9
# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target: # 찾고자 하는 값이 더 작으면
            end = mid - 1 # 왼쪽 부분 탐색
        else: # 찾고자 하는 값이 더 크면
            start = mid + 1 # 오른쪽 부분 탐색
    return 'no'

for request in requests:
    print(binary_search(parts, request, 0, N-1), end=' ')



#  존재하면 yes, 없으면 no 출력



'''
5
8 3 7 9 2
3
5 7 9
'''
