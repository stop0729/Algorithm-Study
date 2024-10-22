# 07. 럭키 스트레이트

# 123402 -> 1+2+3 or 4+0+2 합이 같으면 LUCKY

N = int(input()) # 자릿수 : 항상 짝수

str_N = str(N)
half = int(len(str_N)/2)

sum1 = 0
sum2 = 0

for i in range(half):
    sum1 += int(str_N[i])
    sum2 += int(str_N[i+half])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
