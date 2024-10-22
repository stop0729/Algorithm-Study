# 08. 문자열 재정렬

# 알파벳 오름차순 정렬, 뒤에 모든 숫자 더한 값 출력

S = input() # 문자열 S

# 1
s1 = sorted([s for s in S if s.isalpha()])
s2 = sum(int(s) for s in S if s.isdigit())
print("".join(s1) + str(s2))

# 2
s1 = sorted(filter(str.isalpha, S))
s2 = sum(map(int, filter(str.isdigit, S)))
print("".join(s1) + str(s2))

# K1KA5CB7
# AJKDLSI412K4JSJ9D