# 2447 별 찍기
# https://www.acmicpc.net/problem/2447

def draw_star(matrix, x, y, n): # matrix : 결과를 저장할 2차원 리스트, x, y : 현재 시작 좌표, n : 현재 영역의 크기기
    if n == 1:  # 기본 단위: 별을 찍는다
        matrix[x][y] = '*'
        return
    
    size = n // 3  # 다음 단계의 크기 
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 가운데 영역은 공백
                continue
            draw_star(matrix, x + i * size, y + j * size, size)

def print_stars(n): # n x n 크기의 패턴을 출력하는 함수
    matrix = [[' ' for _ in range(n)] for _ in range(n)]  # 공백으로 초기화 -> 개행문자 문제 해결결
    draw_star(matrix, 0, 0, n)  # 패턴 그리기
    
    # 결과 출력
    for row in matrix:
        print(''.join(row))

N = int(input().strip())  # 입력 받기
print_stars(N)