import random
from math import floor

class HashTable():
    def __init__(self,size=11,mode="chain"):
        if mode == "chain":
            self._A=[[] for i in range(size)]
        if mode == "linear" or mode =="double_hash":
            self._A=[None for i in range(size)]
        self._size=size
        self._mode=mode

    def insert(self,key,value):
        def hash_func(key):
            return (3*int(key)+1)%11
        index=hash_func(key)
        if self._mode == "chain":
            self._A[index].append((key,value))
            return
        if self._mode == "linear":
            for i in range(index,2*self._size):
                if self._A[i%self._size]==None:
                    self._A[i%self._size]=(key,value)
                    return
            raise MemoryError("No memory left for new numbers") 
        if self._mode == "double_hash":
                def second_hash(key):
                    return 7-(key % 7)
                for i in range(2*self._size):
                    if self._A[index]==None:
                        self._A[index]=(key,value)
                        return
                    else:
                        index=(index+second_hash(key))%11

    def display(self):
        print("{")
        for i in range(self._size):
            print("[",end='')
            if self._mode=="chain":
                if self._A[i] != []:
                    for j in range(len(self._A[i])):
                        print(self._A[i][j],end=',')
            if self._mode=="linear" or self._mode=="double_hash":
                print(self._A[i],end='')
            print("]")
        print("}")

test_table=[12,44,13,88,23,94,11,39,20,16,5]

#zad1
t=HashTable(mode="chain")
for i in test_table:
    t.insert(i,"test")
#t.display()    
#zad1

#zad2
t=HashTable(mode="linear")
for i in test_table:
    t.insert(i,"test")
#t.display()    
#zad2

#zad3
t=HashTable(mode="double_hash")
for i in test_table:
    t.insert(i,"test")
#t.display()    
#zad3

#zad4
class Binary_Tree():
    def __init__(self):
        self._A=[None]
        self._size=0
        self.last_empty_index=0
    
    def _resize(self,n):
            if self._size<n:
                for i in range(n-self._size):
                    self._A.append(None)
                return            
    
    def __str__(self):
        return str(self._A)
    def add_element(self,el):
        self._A[self.last_empty_index]=(self.last_empty_index,el)
        self.last_empty_index+=1
        self._resize(self._size+2)
        self._size+=1
    def get_left_child(self,index):
        return 2*index+1
    def get_right_child(self,index):
        return 2*index+2
    def get_parent(self,index):
        if index==0:
            raise ValueError("root has no parent")
        if index%2==0:
            return floor(index/2)-1
        elif index%2==1:
            return floor(index/2) 
t=Binary_Tree()
test_table=[(1,"A"),(2,"B"),(3,"C"),(4,"D"),(5,"E")]
for i in test_table:
    t.add_element(i)
#print(t)

#zad4


#zad6
def max(a,b):
    if a==None:
        if b==None:
            return None
        a=b-1
    if b==None:
        if a==None:
            return None
        b=a-1
    return (abs(a-b)+a+b)/2        

def max_o3(a,b,c):
    m=max(a,b)
    return max(m,c)

class maxheap():
    def __init__(self,starting_list=[]):
        self._A=starting_list
        self._Heapify_all()
    
    def __repr__(self):
        return str(self._A)
    
    def _get_parent(self,index):
        if index%2==0:
            return index//2-1
        if index%2==1:
            return (index-1)//2
    def _get_children(self,index,stop=None):
        if stop==None:
            stop=len(self._A)-1
        if (2*index)+1>stop:
            return [None,None]
        if (2*index)+2>stop:
            return [(2*index)+1,None]
        return [(2*index)+1,(2*index)+2]        
    def _heapify_up(self,index):
        while index!=0:
            if self._A[index]>self._A[self._get_parent(index)]:
                temp=self._A[self._get_parent(index)]
                self._A[self._get_parent(index)]=self._A[index]
                self._A[index]=temp
                index=self._get_parent(index)
                #print(self._A)
            else:
                break        
    def _heapify_down(self,index,stop=None):
        while index!=None:
            b,c=self._get_children(index,stop)
            if b==None:
                temp_b=None
            else:
                temp_b=self._A[b]
            if c==None:
                temp_c=None
            else:
                temp_c=self._A[c]
                        
            if self._A[index]!=max_o3(self._A[index],temp_b,temp_c):
                if c==None or self._A[c]<=self._A[b]:
                    temp=self._A[b]
                    self._A[b]=self._A[index]
                    self._A[index]=temp
                    index=b
                else:
                    temp=self._A[c]
                    self._A[c]=self._A[index]
                    self._A[index]=temp
                    index=c
            else:
                break                
    def heapsort(self):
        stop=len(self._A)-1
        while stop!=0:
            temp=self._A[stop]
            self._A[stop]=self._A[0]
            self._A[0]=temp
            stop-=1
            self._heapify_down(0,stop)


    def _Heapify_all(self):
        for i in range(len(self._A)):
            self._heapify_up(i)

test_table=random.choices(population=range(0,101),k=20)
a=maxheap(starting_list=test_table)
a.heapsort()
print(a)


# [0, 1 2, 3 4 5 6]
#zad6