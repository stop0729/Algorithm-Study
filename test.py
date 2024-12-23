while True:
    sides = list(map(int, input("Enter three sides (0 to exit): ").split()))
    if sides[0] == 0:
        break
    
    sides.sort()  # 세 숫자를 정렬하여 가장 큰 숫자가 c가 되도록
    a, b, c = sides  # 정렬된 값을 다시 a, b, c에 할당
    
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")