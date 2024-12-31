# def binary_search(array, target, start, end):
#     if start > end:
#         return start
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)

# result = binary_search([1, 3, 5, 7, 8, 10, 12, 18], 9, 0, 7)
# print(result)

N, target = map(int, input().split())
array = list(map(int, input().split()))

long = max(array)
def binary_search(array, target, start, end):
    if start > end:
        print('aaaaaaaaa')
        return start
    mid = (start + end) // 2
    if sum(array) - len(array) * mid == target:
        print('aaaaaaaaa')
        return mid
    elif sum(array) - len(array) * mid > target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
    
result = binary_search(array, target, 0, long)
print(result)
    