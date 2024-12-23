# https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())

# r행 c열을 몇 번째로 방문하는지 계산
def z(n, r, c):
    if n == 0:
        return 0
    # 배열을 크기가 2^(n-1) × 2^(n-1)로 4등분 한 후에 재귀적으로 순서대로 방문
    
    # half = 작은 배열의 한 변의 길이
    half = 1 << (n-1) # 1 * 2^(n-1)
    # 왼쪽 위(1번 사분면)
    if r < half and c < half:
        return z(n - 1, r, c)
    # 오른쪽 위(2번 사분면)
    if r < half and c >= half:
        return half * half + z(n - 1, r, c - half)
    # 왼쪽 아래(3번 사분면)
    if r >= half and c < half:
        return 2 * half * half + z(n - 1, r - half, c)
    # 오른쪽 아래(4번 사분면)
    return 3 * half * half + z(n - 1, r - half, c - half)

print(z(N, r, c))