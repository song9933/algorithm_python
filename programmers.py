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

def sol_3(n):
    answer = 0
    num = pow(n, 0.5) 
    if num == int(num) :
        answer = pow(num + 1, 2)
    else :
        answer = -1
    return answer  

#약수의 합
def sol_4(n):
  answer = 0
  for i in range(1, n+1):
    if n%i ==0:
      answer += i
  return answer