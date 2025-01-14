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



# Try 1
# N, target = map(int, input().split())
# array = list(map(int, input().split()))

# long = max(array)
# record = 0

# def binary_search(array, target, start, end, record):
#     if start > end:
#         print(start, end, record)
#         print('aaaaaaa')
#         return record
#     mid = (start + end) // 2
#     total = 0
#     for x in array:
#         if x > mid:
#             total += x - mid
#     if total == target:
#         return mid
#     elif total > target:
#         print('bbbbbbbb', mid+1, end, mid, total)
#         return binary_search(array, target, mid+1, end, mid)
#     else:
#         print('cccccccc', start, mid-1, mid, total)
#         return binary_search(array, target, start, mid-1, mid)
    
# result = binary_search(array, target, 0, long, record)
# print(result)



# Try 2
# n, m = list(map(int, input().split()))
# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# result = 0
# while(start <= end):
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         if x > mid:
#             total += x - mid
#     if total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1


# print(result)
    