# -*- coding: utf-8 -*-
"""
Class stack and queue

@author: Park Jieun
"""
class Stack:
    __length = False
    
    def __init__(self):#초기화
        self.stack_list = []
        
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, newLength):
        self.__length = newLength
    
    def push(self, value):
        if self.__length != False: #가변길이가 아니라면 즉 고정길이 일 때만 크기 검사
            if len(self.stack_list) > self.__length-1:
                print("Stack is full")
                return 
        self.stack_list.append(value)
        
    def pop(self):
        if len(self.stack_list) < 1:#스택이 비어있을 때 오류
            print("Stack is empty")
            return 
        print("pop: "+str(self.stack_list.pop()))
        
    def stack_print(self):#스택 출력
        print("stack = ",self.stack_list)
        
class Queue:
    __length = False
    
    def __init__(self):
        self.queue_list = []
        
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, newLength):
        self.__length = newLength
    
    def enqueue(self, value):
        if self.__length != False: #가변길이가 아니라면 즉 고정길이 일 때만 크기 검사
            if len(self.queue_list) > self.__length-1:
                print("Queue is full")
                return 
        self.queue_list.append(value)
        
    def dequeue(self):
        if len(self.queue_list) < 1:#스택이 비어있을 때 오류
            print("Queue is empty")
            return 
        print("dequeue: "+str(self.queue_list.pop(0)))
        
    def queue_print(self):#큐 출력
        print("queue = ",self.queue_list)

                    
 
if __name__ == "__main__":# main namespace를 의미합니다.
    test = Stack()
    test.length = 3
    print(test.length)
    test.pop()
    test.push(1)
    test.push(2)
    test.push(3)
    test.stack_print()
    test.push(4)
    test.pop()
    test.stack_print()
    print("\n")

    Qtest = Queue()
    print(Qtest.length)
    Qtest.length = 3
    Qtest.dequeue()
    Qtest.enqueue(1)
    Qtest.enqueue(2)
    Qtest.enqueue(3)
    Qtest.enqueue(4)
    Qtest.dequeue()
    Qtest.queue_print()
    
    
    