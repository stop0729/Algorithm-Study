# 부분수열의 합
# https://www.acmicpc.net/problem/1182

def dfs(n, sum, cnt): # n: 현재 숫자, sum: 현재까지의 합, cnt: 현재까지의 개수
    global ans
    # 종료 조건, 정답 처리
    if n == N:
        if sum == S and cnt > 0:
            ans += 1
        return
    # 하부단계(함수) 호출
    dfs(n+1, sum+lst[n], cnt+1) # 포함하는 경우
    dfs(n+1, sum, cnt) # 포함하지 않는 경우

N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0,0,0)
print(ans)

#                          0
#     1포함       1미포함           2포함      2미포함
# 2포함 2미포함 2포함 2미포함 
# ....