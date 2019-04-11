# -*- coding: utf-8 -*-
"""
GCD and LCM
최대공약수와 최소공배수 

1) 유클리드 호제법으로 최대공약수 구하기
  a = bq+r이면 a와 b의 최대공약수는 b와 r의 최대공약수와 같다
  따라서 a mod b = 0이면 GCD(a,b) = b이고,
  a mod b != 0이면 GCD(a,b) = GCD(b, a mod b)이다.

2) 최소공배수
x = ab, y = bc이면, x와 y의 최대공약수는 b
최소공배수는 abc다. 따라서 최소공배수는 두 수를 곱하여 
최대공약수로 나눈 것과 같다.( abc = xy/b)
@author: Park Jieun

"""
#최대공약수를 구하는 함수
def GCD(num1,num2):
    mod = num1%num2
     """나머지가 0이면 바로 num2를 반환,
     0이 아니면 나머지가 0이 되는 순간까지 다음 과정을 반복"""
    while mod > 0:
        num1 = num2 
        num2 = mod
        mod = num1%num2
    return num2

#최소공배수를 구하는 함수
#두 수를 곱하여 최대공약수로 나눈 값을 반환.
def LCM(num1, num2):
    return (num1*num2)/GCD(num1,num2) 

print(GCD(4, 12))
print(LCM(180, 72))