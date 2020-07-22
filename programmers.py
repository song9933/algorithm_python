def sol_1(seoul):
  idx = seoul.index("Kim")
  print(f"김서방은 {idx}에 있다")


def sol_2(arr, divisor):
    check = 0
    answer = []
    for i in arr:
        if i%divisor == 0:
            check+=1
            answer.append(i)        
    if check == 0 :
        answer = [-1]
    answer.sort()
    print (answer )
