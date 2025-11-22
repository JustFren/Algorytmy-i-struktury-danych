import ctypes #tablice niskopoziomowe
import matplotlib.pyplot as plt
import random
import time
import copy
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
print("zad1")
check_1()
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
        

    fig, ax = plt.subplots(1,3)
    x=range(N)
    ax[0].plot(x ,t_1, label="append")
    ax[0].set_xlabel("list size")
    ax[0].set_ylabel("time(ns)")
    ax[0].set_title("append")
    ax[1].plot(x ,t_2, label="extend")
    ax[1].set_xlabel("list size")
    ax[1].set_ylabel("time(ns)")
    ax[1].set_title("extend")
    
    
    ax[2].plot(x ,t_1, label="append")
    ax[2].set_xlabel("list size")
    ax[2].set_ylabel("time(ns)")
    ax[2].set_title("append vs extend")
    ax[2].plot(x ,t_2, label="extend")
    ax[2].legend()

    plt.show()

#zad4

#zad5
class Queue:
    DEFAULT_CAPACITY = 16
    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def __str__(self):
        return str(self._data)
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

def check_5():
    q=Queue()
    for i in range(16):
        q.enqueue(i)
    print(q)    
    for i in range(8):
        q.dequeue()    
    print(q)


#zad5

#zad6
class deque(Queue):
    def __init__(self):
        super().__init__()
        self.back=0
    def add_first(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._size+=1
        for i in range(self._size):
            temp=self._data[i]
            self._data[i]=e
            e=temp
            #print(self._data)

    def add_last(self,e):
        self.enqueue(e)
    def delete_first(self):
        self.dequeue()
    def delete_last(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        if self._size < len(self._data)//2:
            self._resize(len(self._data)//2+1)
        self._size-=1
        self._data[self._size]=None    

    def first(self):
        return self._data[0]
    def last(self):
        return self._data[self._size-1]
def check_6():
    d = deque()
    for i in range(10):
        d.add_last(i)
    print(d)
    d.add_first(100)
    d.delete_first()
    d.delete_last()


#zad6

#zad7
class Empty(Exception):
    pass

class stack():
    def __init__(self):
        self._data = [] #nowy pusty stos
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    def __str__(self):
        return str(self._data)
    
def check_html(str):
    s=stack()
    str+=' '
    for i in range(len(str)):
        if str[i]=='<':
            begin=i
        if str[i]=='>':
            end=i+1
            last=None
            try:
                last=s.top()
            except:
                pass
            temp=str[begin:end]
            s.push(temp)
            if temp[1]=='/':
                if last == None:
                    return False
                if last[1:] == temp[2:]:
                    s.pop()
                    s.pop()
                else :
                    return False
    if len(s)>0 :
        return False            
    return True

def check_7():
    html_strings=["<html><head><title>T</title></head><body><div><p>OK</p></div></body></html>"\
              ,"<html><body><p>Tekst<div>coś</div></body></html>"\
              ,"<div><span>Tekst</div></span>"\
              ,"<html><body><ul><li>1<li>2</ul></body></html>"
             ]
    for str in html_strings:
        print(check_html(str))

#zad7

#zad8
def perms(n):
    temp = [[],[*range(n)]]
    s=stack()
    s.push(temp)
    out=[]
    while len(s)!=0:
        temp=s.top()
        if len(temp[1])==0:
            out.append(temp[0])
            s.pop()
            continue
        s.pop()
        #print(temp)
        #print()
        for i in range(len(temp[1])):
            temp2=copy.deepcopy(temp[0])
            temp2.append(temp[1][i])
            temp3=copy.deepcopy(temp[1])
            temp3.remove(temp[1][i])
            
            s.push([temp2,temp3])
        
        #print(s)


    return out

#zad8

#zad9
class stack_with_queue(Queue):
    def __init__(self):
        super().__init__()
    #złożoność O(1)
    def push(self,e):
        self.enqueue(e)
    #złożoność O(1)
    def pop(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        if self._size < len(self._data)//2:
            self._resize(len(self._data)//2+1)
        self._size-=1
        temp=self._data[self._size]
        self._data[self._size]=None
        return temp
    #złożoność O(1) 
    def top(self):
        return self._data[self._size-1]      
def check_9():
    s=stack_with_queue()
    for i in range(10):
        s.push(i)
    print(s)
    s.top()
    s.pop()
    print(s)
#zad9

#zad10
class queue_with_stack():
    def __init__(self):
        self._main=stack()
        self._dump=stack()
    def __str__(self):
        return str(self._main)
    def __len__(self):
        return len(self._main)
    def isEmpty(self):
        return len(self._main) == 0 
    def first(self):
        while len(self._main)!=1:
            self._dump.push(self._main.pop())    
        out=self._main.top()
        while len(self._dump)!=0:
            self._main.push(self._dump.pop())
        return out

    def enqueue(self,e):
        self._main.push(e)
    def dequeue(self):
        while len(self._main)!=1:
            self._dump.push(self._main.pop())    
        out=self._main.top()
        self._main.pop()
        while len(self._dump)!=0:
            self._main.push(self._dump.pop())
        return out

def check_10():
    q=queue_with_stack()
    for i in range(16):
        q.enqueue(i)
    print(q)    
    for i in range(8):
        q.dequeue()    
    print(q)
    print(q.first())
    print(q.isEmpty())
#zad10

print("zad1")
check_1()
print("\nzad2")
check_2()
print("\nzad3")
check_3(10)
print("\nzad4")
check_4()
print("\nzad5")
check_5()
print("\nzad6")
check_6()
print("\nzad7")
check_7()
print("\nzad8")
print(perms(3))
print("\nzad9")
check_9()
print("\nzad10")
check_10()