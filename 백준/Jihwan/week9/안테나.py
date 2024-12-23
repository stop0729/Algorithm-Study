N = int(input())

lst = list(map(int, input().split()))

lst.sort()

if N % 2 ==0:
    a = N // 2
    print(lst[a-1])
else:
    a = N//2 + 1
    print(lst[a-1])