def rotate(cdn): # cdn = coordinate
    a, b = cdn
    a[0] = a[0] + 1
    a[1] = a[1] + 1
    a, b = b, a
    cdn = [a, b]
    return cdn

def move_right(cdn): # 
    a, b = cdn
    a = [a[0], a[1]+1]
    b = [b[0], b[1]+1]
    cdn = [a,b]
    return cdn

def move_down(cdn):
    a, b = cdn
    a = [a[0]+1, a[1]]
    b = [a[0]+1, b[1]]
    cdn = [a,b]
    return cdn

def solution(board):

    cdn = [[1,1], [1,2]]
    answer = 0
    a, b = cdn
    print(a,b)

    
    length = len(board)
    while b != [length, length]:
        if a[0] == b[0]: # 가로로 놓여있다면
            print(cdn)
            if b[1] == length:
                cdn = rotate(cdn)
                answer += 1
                a, b = cdn
            elif board[b[0]-1][b[1]] == 1: # 막혀있다면
                cdn = rotate(cdn)
                answer += 1
                a, b = cdn
            else: # 안 막혀있다면
                cdn = move_right(cdn)
                answer += 1
                a, b = cdn
        elif a[1] == b[1]: # 세로로 놓여있다면
            print(cdn)
            if b[0] == length:
                cdn = rotate(cdn)
                answer += 1
                a, b = cdn
            elif board[b[0]][b[1]-1] == 1: # 막혀있다면
                cdn = rotate(cdn)
                answer += 1
                a, b = cdn
            else:
                cdn = move_down(cdn)
                answer += 1
                a, b = cdn
    print(answer)
    return answer
                
                

board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]

solution(board)


'''
0 0 0 0 0 0 1
1 1 1 1 0 0 1
0 0 0 0 0 0 0 
0 0 1 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 1 1
0 0 1 0 0 0 0
'''

queue([[a],[b]]).popleft()

dx1 = [1,-1,0,0,]
dy1 = [0,0,1,-1,]