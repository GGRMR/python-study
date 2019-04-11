# -*- coding: utf-8 -*-
"""
fibonacci

@author: Park Jieun

"""
#피보나치 수열 함수

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fibo(n-2)+fibo(n-1)
    
num = int(input("숫자 입력: "))

#입력받은 수까지의 수열 출력
for i in range(1, num+1):
    print(fibo(i))

