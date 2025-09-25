def fibonacci_print(n):
    '매개변수로 들어온 n 값 미만의 피보나치 수열을 출력하는 함수'
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fibonacci(n):
    'n미만의 피보나치수열을 리스트로 출력'
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


#피보나치 수열 관련 함수들 테스트(cmd 창에서 python fibonacci.py 100)
if __name__ == '__main__':
    import sys
#    print(sys.argv) #argv : cmd창에 입력한 python 뒤의 값들을 뛰어쓰기로 나누어 리스트에 저장 0번은 항상 파일이름
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("몇까지의 피보나치 수열을 찾으시나요? "))
    print("1. print test :", end=' ')
    fibonacci_print(n)
    print("2. return test :", fibonacci(n))