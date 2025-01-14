def binary_search1(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if mid == 0 and array[mid] == target:
        return mid
    if array[mid] == target and array[mid-1] != target:
        return mid
    elif array[mid] == target and array[mid-1] == target:
        return binary_search1(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search1(array, target, mid+1, end)
    elif array[mid] > target:
        return binary_search1(array, target, start, mid-1)
    
def binary_search2(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target and mid == len(array)-1:
        return mid
    elif array[mid] == target and array[mid+1] != target:
        return mid
    elif array[mid] == target and array[mid+1] == target:
        return binary_search2(array, target, mid+1, end)
    elif array[mid] < target:
        return binary_search2(array, target, mid+1, end)
    elif array[mid] > target:
        return binary_search2(array, target, start, mid-1)
    
N, x = map(int, input().split())
array = list(map(int, input().split()))

result1 = binary_search1(array, x, 0, N-1)
result2 = binary_search2(array, x, 0, N-1)

if result1 != None:
    print(result2 - result1 + 1)
else:
    print(-1)