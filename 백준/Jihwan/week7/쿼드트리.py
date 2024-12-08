n = int(input())

pixel = []
for i in range(n):
    pixel.append(list(map(int, input())))


def tree(row, col, n):
    current = pixel[row][col]
    
    for i in range(row, row+n):
        for j in range(col, col+n):
            if current != pixel[i][j]:
                print('(', end='')
                n_next = n//2
                for k in range(2):
                    for l in range(2):
                        tree(row+(n_next)*k, col+(n_next)*l, n_next)
                print(')', end='')
                return
            
    print(current, end='')

    return

tree(0, 0, n)