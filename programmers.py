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

#제일 작은 수 제거하기
def sol_5(arr):
    answer = [
    if (len(arr) <= 1):
        answer = [-1]
    else :
        arr.remove(min(arr))
        answer = arr
    return answer

#두 정수 사이의 합
def sol_6(a, b):
    answer = 0
    if a>b:
        for i in range(b, a+1):
            answer += i
    elif b>a:
        for i in range(a, b+1):
            answer += i
    else :
        answer = a
    return answer    

#자연수 뒤집어 배열로 만들기
def sol_7(n):
    answer = list(map(int,reversed(str(n))))
    return answer

#최대공약수, 최소공배수
def sol_8(n,m):
    for i in range(1, n+1):
        if n%i == 0 :
            if m%i ==0:
                gcd = i
    if gcd == 1:
        lcm = n*m
    else :
        lcm = gcd*(n//gcd)*(m//gcd)
    return [gcd, lcm]

#소수찾기 
def sol_9(n):
    a_set = set(range(2, n+1))
    for i in range(2, n+1) :
        if i in a_set:
            a_set -= set(range(i*2, n+1, i))
    return len(a_set)

#자릿수 더하기
def sol_10(n):
    answer = 0
    num = list(map(int, str(n)))
    return sum(num)    

#x만큼 간격이 있는 n개의 숫자
def sol_11(x, n):
    answer = []
    for i in range(1, n+1) :
        answer.append(x*i)
    return answer

#이상한 문자 만들기    
def sol_12(s):
    a_list = s.split(" ")
    answer = []
    for a in a_list :
        s =""
        for i in range(0, len(a)):
            s += a[i].upper() if i%2 == 0 else a[i].lower()
        answer.append(s)
    return ' '.join(answer)