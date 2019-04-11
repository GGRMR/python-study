# -*- coding: utf-8 -*-
"""
stack_functions
함수와 리스트를 이용해서 스택 구현하기

@author: Park Jieun

"""

def pop(stack = []): #== def pop(stack)
    stack.pop()
    return stack

def push(stack = []):
    value = input("PUSH: ")
    stack.insert(len(stack)+1, value)
    return stack

def stack_list(stack = []):
    print("stack = ",stack)
    


myList = [1, "fruit", 3, 5, 8, "Jieun"]

stack_list(myList)

pop(myList)
stack_list(myList)

push(myList)
stack_list(myList)


