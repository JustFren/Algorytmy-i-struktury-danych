import ctypes #tablice niskopoziomowe
import matplotlib.pyplot as plt
import random
import time
#zad1
class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self,c):
        return (c*ctypes.py_object)()
    
    def __str__(self):
        out=''
        out+="[ "
        for i in range(self._n):
            out+=f"{self._A[i]}, "
        out+="]"
        return out

    def insert(self,k,value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        
        if k == self._n-1:
            self.append(value)   
        
        B=self._make_array(self._capacity)
        for i in range(k):
            B[i]=self._A[i]
        B[k]=value
        for i in range(k+1,self._n+1):
            B[i]=self._A[i-1]
        self._n+=1
        self._A=B   

        #for i in range(len(B)):
        #    print(B[i])

    def remove(self,value):
        k=-1
        for i in range(self._n):
            if self._A[i] == value:
                k=i
                break
        if k == -1:
            raise ValueError("value isnt in array")
        
        B=self._make_array(self._capacity)
        for i in range(k):
            B[i]=self._A[i]
        for i in range(k,self._n-1):
            B[i]=self._A[i+1]
        self._n-=1
        self._A=B

    def expand(self,seq):
        for i in range(len(seq)):
            self.append(seq[i])
        
def check_1():        
    a=DynamicArray()
    a.expand([i for i in range(10)])
    print(a)
    a.insert(0,10)
    print(a)
    a.remove(3)
    print(a)
#zad1

#zad2
def check_2():
    N=100_000
    master_list = random.choices(range(21),k=N)
    t_1=[]
    t_2=[]
    t_3=[]
    t_4=[]
    for i in range(10,N,10):
        temp_list=master_list[:i]
        begin = time.time_ns()
        temp_list.pop(0)
        end = time.time_ns()
        t_1.append(end-begin)
        
        temp_list=master_list[:i]
        begin = time.time_ns()
        temp_list.pop(i//3)
        end = time.time_ns()
        t_2.append(end-begin)

        temp_list=master_list[:i]
        begin = time.time_ns()
        temp_list.pop(2*(i//3))
        end = time.time_ns()
        t_3.append(end-begin)

        temp_list=master_list[:i]
        begin = time.time_ns()
        temp_list.pop(i-1)
        end = time.time_ns()
        t_4.append(end-begin)     



    fig, ax = plt.subplots(2,2)
    x=range(10,N,10)
    ax[0,0].plot(x ,t_1, label="pop(0)")
    ax[0,0].set_xlabel("list size")
    ax[0,0].set_ylabel("time(ns)")
    ax[0,0].set_title("pop(0)")
    
    ax[0,1].plot(x ,t_2, label="pop(i//3)")
    ax[0,1].set_xlabel("list size")
    ax[0,1].set_ylabel("time(ns)")
    ax[0,1].set_title("pop(i//3)")

    ax[1,0].plot(x ,t_3, label="pop(2*(i//3))")
    ax[1,0].set_xlabel("list size")
    ax[1,0].set_ylabel("time(ns)")
    ax[1,0].set_title("pop(2*(i//3))")

    ax[1,1].plot(x ,t_4, label="pop(i-1)")
    ax[1,1].set_xlabel("list size")
    ax[1,1].set_ylabel("time(ns)")
    ax[1,1].set_title("pop(i-1)")
    
    plt.show()
#zad2

#zad3
def check_3(n):
    list=[]
    for i in range(n):
        temp=random.choices(range(-10,10),k=n)
        print(temp)
        list.append(temp) 

    def sum_of_table(table):
        res=0
        for i in range(len(table)):
            res+=sum(table[i])
        return res    

    print(f"sum is {sum_of_table(list)}")
#zad3

#zad4
def check_4():
    N=10_000
    master_list=random.choices(range(-10,10),k=N)
    s_list=[i for i in range(10)]
    t_1=[]
    t_2=[]
    for i in range(N):
        temp=s_list
        begin = time.time_ns()
        for j in range(i):
            temp.append(master_list[j])
        end = time.time_ns()
        t_1.append(end-begin)
        temp=s_list
        begin = time.time_ns()
        temp.extend(master_list[:i])
        end = time.time_ns()
        t_2.append(end-begin)
        

    fig, ax = plt.subplots(1,2)
    x=range(N)
    ax[0].plot(x ,t_1, label="pop(0)")
    ax[0].set_xlabel("list size")
    ax[0].set_ylabel("time(ns)")
    ax[0].set_title("append")
    ax[1].plot(x ,t_2, label="pop(i//3)")
    ax[1].set_xlabel("list size")
    ax[1].set_ylabel("time(ns)")
    ax[1].set_title("extend")
    plt.show()
#zad4

#zad5
class Queue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        if self._size < len(self._data)//2:
            self._resize(len(self._data)//2+1)
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return value
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
    def _resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0
#zad5

#zad6