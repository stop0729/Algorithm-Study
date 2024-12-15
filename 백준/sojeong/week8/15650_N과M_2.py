# N과 M (2)
# https://www.acmicpc.net/problem/

def dfs(start, lst): # n : 지금까지 선택한 숫자 개수, lst : 지금까지 선택한 숫자들
    # 종료 조건(n에 관련) + 정답처리
    if len(lst)==M: # M개의 수열을 완성 # n==M
        ans.append(lst)
        return
    
    # 하부단계(함수) 호출
    for j in range(start, N+1): # start부터 시작
        if v[j]==0: # 선택하지 않은 숫자인 경우추가
            v[j] = 1
            dfs(j+1, lst+[j]) # start를 j+1로 바꿔줌
            v[j] = 0

N, M = map(int, input().split())

ans = []  # 정답 리스트를 저장할 리스트
v = [0]*(N+1) # 중복확인을 위한 visited[]

dfs(1, []) # 1부터 시작
for lst in ans:
    print(*lst) # 리스트를 풀어서 출력