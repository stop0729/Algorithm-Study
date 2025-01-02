# 정렬된 배열에서 특정 수의 개수 구하기

# nums에서 값이 x인 원소의 개수를 출력
# 시간복잡도 O(logN)으로 설계해야함

# 처음과 끝 인덱스 찾기
def start_end_index(array, x):
    
    s = binary_search_start(array, x, 0, len(array)-1)
    e = binary_search_end(array, x, 0, len(array)-1)
    
    if s == None or e == None:
        return -1
    else:
        return e - s + 1

# 시작 인덱스 찾기기
def binary_search_start(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if mid == 0 or array[mid-1] < target: # x가 처음 등장하는 위치 바로 전 값이 x보다 작을 때
                return mid
            else: # x가 mid보다 더 앞에 있다는 거니까
                end = mid - 1 # 왼쪽 부분 탐색
        elif array[mid] > target: # 찾고자 하는 값이 더 작으면
            end = mid - 1 # 왼쪽 부분 탐색
        else: # 찾고자 하는 값이 더 크면
            start = mid + 1 # 오른쪽 부분 탐색
    return None

# 끝 인덱스 찾기기
def binary_search_end(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if mid == len(array)-1 or array[mid+1] > target: # x가 처음 등장하는 위치 바로 뒤가 x보다 클클 때
                return mid
            else: # x가 mid보다 더 뒤에 있다는 거니까
                start = mid + 1 # 오른쪽 부분 탐색
        elif array[mid] > target: # 찾고자 하는 값이 더 작으면
            end = mid - 1 # 왼쪽 부분 탐색
        else: # 찾고자 하는 값이 더 크면
            start = mid + 1 # 오른쪽 부분 탐색
    return None

N , x = map(int, input().split())
nums = list(map(int, input().split()))

result = start_end_index(nums, x)
print(result)


'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''