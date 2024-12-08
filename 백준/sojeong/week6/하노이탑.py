# https://www.acmicpc.net/problem/1914

K = int(input())

# 이동 과정을 저장하기 위한 리스트
moves = []

def hanoi(n, start, end):
    if n == 1:
        moves.append(f"{start} {end}")
        return
    hanoi(n - 1, start, 6 - start - end)  # 첫 번째 이동: n-1개의 원반을 중간 기둥으로 이동
    moves.append(f"{start} {end}")        # 현재 원반을 목적 기둥으로 이동
    hanoi(n - 1, 6 - start - end, end)    # 중간 기둥의 n-1개의 원반을 목적 기둥으로 이동

# 하노이 탑 계산
hanoi(K, 1, 3)

# 출력
print(len(moves))  # 총 이동 횟수
print("\n".join(moves))  # 이동 과정

# 3
'''
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''
