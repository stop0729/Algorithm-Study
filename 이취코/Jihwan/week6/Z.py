N, r, c = map(int, input().split())

def find(N, r, c):
    if N == 0:
        return 0
    half = 2**(N-1)
    if r<half and c<half:
        return find(N-1, r, c)
    if r>=half and c<half:
        return 2 * half*half + find(N-1, r-half, c)
    if r<half and c>=half:
        return half*half + find(N-1, r, c-half)
    if r>=half and c>=half:
        return 3 * half*half + find(N-1, r-half, c-half)
    
result = find(N, r, c)
print(result)