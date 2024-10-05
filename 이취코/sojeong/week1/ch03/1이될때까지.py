# 1이 될 때까지

# 1. N-1
# 2. N/K (N이 K로 나누어떨어질 때만)

N, K = map(int, input().split())

count = 0

while N > 1:
    if N%K==0:
        N /= K
    else:
        N -= 1
    count += 1

print(count)