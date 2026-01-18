import matplotlib.pyplot as plt
import random
import time
import math
#zad 1
class Node():
    def __init__(self,data,parent=None):
          self.parent=parent
          self.data=data
          self.children=[None,None]


class Binary_search_Tree():
    def __init__(self,root_value):
        self.root = Node(root_value)
    
    def __str__(self):
        out=[self.root]
        def traverse(node,out):
            if node.children!=[None,None]:
                if node.children[0]!=None:
                    out.append(node.children[0])
                if node.children[1]!=None:
                    out.append(node.children[1])
                if node.children[0]!=None:
                    traverse(node.children[0],out)
                if node.children[1]!=None:
                    traverse(node.children[1],out)    
        traverse(self.root,out)
        for i in range(len(out)):
            out[i]=out[i].data
        return str(out)
    
    def add_node(self,data,parent):
        new_node=Node(data,parent)
        if parent.children[0]==None and data<parent.data:
            parent.children[0]=new_node
            return    
        if parent.children[1]==None and data >=parent.data:
            parent.children[1]=new_node
            return
        if parent.children[0]!=None and data<parent.data:
            self.add_node(data,parent.children[0])
            return
        if parent.children[1]!=None and data>=parent.data:
            self.add_node(data,parent.children[1])
            return

    def find(self,value):
        new_node=self.root
        def _find(value,new_node):
            if value == new_node.data:
                return new_node
            if new_node.children[0]!=None and value < new_node.data:
                new_node=new_node.children[0]
                return _find(value,new_node)
            if new_node.children[1]!=None and value >= new_node.data:
                new_node=new_node.children[1]
                return _find(value,new_node)
            return None
        return _find(value,new_node)
t=Binary_search_Tree(7)
t.add_node(8,t.root)
t.add_node(9,t.root)
print(t.find(9))
#zad 1

#zad 2
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
    def add_element(self,value):
        self._A.append(value)
        self._heapify_up()

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

rand=random.choices(range(-50,50),k=1000)
times=[]
for i in range(10,1000):
    h=maxheap(rand[:i])
    start_time=time.time_ns()
    h.heapsort()
    end_time=time.time_ns()
    times.append(end_time-start_time)

x=range(len(times))
y1=[500*n*math.log(n) for n in range(1,len(x))]
y2=[575*n*math.log(n) for n in range(1,len(x))]

fig,ax=plt.subplots(nrows=1,ncols=1)
ax.plot(x,times,color="cyan",label="dane eksperymentlne")
ax.plot(x[1:],y1,color="orange",label="C*n*log(n)")
ax.plot(x[1:],y2,color="orange")
ax.set_title("analiza eksperymentalna heapsort")
ax.set_xlabel("wielkość tablicy")
ax.set_ylabel("czas (ns)")
ax.legend()
plt.show()

#zad 2

#zad 3
class max_n_heap():
    def __init__(self,n,starting_list=[]):
        self._A=starting_list
        self._Heapify_all()
        self.n=n
    def __repr__(self):
        return str(self._A)
    def add_element(self,value):
        self._A.append(value)
        self._heapify_up()
        self.heapsort()
        self._A.pop(0)
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


#zad3            