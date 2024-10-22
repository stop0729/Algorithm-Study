S = list(input())
S.sort()
number = ['1','2','3','4','5','6','7','8','9']
result = 0
for i in range(len(S)):
    if S[i] in number:
        result += int(S[i])
    else:
        result = str(result)
        temp = ''.join(S[i:])
        result = str(temp) + result
        break

print(result)