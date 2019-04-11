# -*- coding: utf-8 -*-
"""
queue functions
함수와 리스트를 이용해서 큐 구현하기

@author: Park Jieun

"""
def enqueue(queue = []): # == def enqueue(queue)
    value = input("enqueue: ")
    queue.append(value)
    return queue

def dequeue(queue = []):
    queue.pop(0)
    return queue

def list_queue(queue = []):
    print("queue = ", queue)
    
myList = [1, "fruit", 3, 5, 8, "Jieun"]

list_queue(myList)

enqueue(myList)
list_queue(myList)

dequeue(myList)
list_queue(myList)

