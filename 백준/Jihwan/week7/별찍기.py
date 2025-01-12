a = int(input())
lst = [[' ']*a for i in range(a)]
def fill(a, b):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            lst[a+i][b+j] = '*' 

def star(a, b, c):
    if c == 3:
        fill(a, b)
        return
    else:
        c = c // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star(a + i*c, b + j*c, c)

star(0, 0, a)

for i in range(a):
    for j in range(a):
        print(lst[i][j], end = '')
    print()

