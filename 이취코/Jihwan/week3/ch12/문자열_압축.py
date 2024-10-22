word = input()
result = 10000

def check(a, b):
    if word[a:a+b] == word[a+b:a+2*b]:
        return True
    else:
        return False

for i in range(1, len(word)//2 + 1):
    switch = 0
    time = 0
    string = ""
    for j in range(0,len(word)-2*i,i):

        if check(j, i) and switch == 0:
            time = 2
            string = string + word[j:j+i]
            switch = 1
        elif check(j, i) and switch == 1:
            time += 1
        elif (check(j, i) == False) and switch == 1:
            string = string + str(time)
            string = string + word[j:j+i]
            switch = 0
            time = 0
        else:
            string = string + word[j:j+i]

        if j + 2*i == len(word)-1 :
            if check(j, i) and switch == 0:
                string = string + '2' + word[j:j+i]
            elif check(j, i) and switch == 1:
                string = string + str(time)
            else:
                string += word[j:j+i]
    print(string)
    if result > len(string):
        result = len(string)

print(result)