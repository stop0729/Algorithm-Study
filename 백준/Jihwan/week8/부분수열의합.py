N, S = map(int, input().split())

lst = list(map(int, input().split()))
result = 0

def func(cur, tot):
    global result
    if cur == N:
        if tot == S:
            result += 1
        return
    func(cur+1, tot)
    func(cur+1, tot+lst[cur])

func(0,0)
if S == 0:
    result -= 1
print(result)