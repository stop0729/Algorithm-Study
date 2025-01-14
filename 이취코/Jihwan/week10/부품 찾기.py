import sys
def binary_search1(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif array[mid] > target:
        return binary_search1(array, target, start, mid-1)
    else:
        return binary_search1(array, target, mid+1, end)
    
    
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n = int(sys.stdin.readline().rstrip())
store = list(map(int, sys.stdin.readline().rstrip().split()))
store.sort()

m = int(sys.stdin.readline().rstrip())      
client = list(map(int, sys.stdin.readline().rstrip().split()))

for i in client:
    result = binary_search1(store, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')