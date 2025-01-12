N = input()
middle = len(N) // 2

r1 = 0
r2 = 0
for i in range(middle):
    r1 += int(N[i])
    r2 += int(N[i+middle])

if r1 == r2:
    print('LUCKY')
else:
    print("READY")