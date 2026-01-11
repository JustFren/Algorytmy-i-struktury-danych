import matplotlib.pyplot as plt

import random
from math import floor
import time

#zad 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def first(self):
        return self.head.data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

class stack(LinkedList):
    def push(self,el):
        self.prepend(el)
    def pop(self):
        temp=self.first()
        self.delete(self.first())
        return temp
    def top(self):
        return self.first()
n=50    
val=random.choices(range(101),k=n)

list_list=[[val[j] for j in range(i)] for i in range(10,n)]
#print(list_list)
times=[[],[]]
for i in range(len(list_list)):
    #push
    temp=stack()

    for j in range(len(list_list[i])-2):
        temp.push(list_list[i][j])
    start_time=time.time_ns()
    temp.push(list_list[i][len(list_list[i])-1])
    end_time=time.time_ns()
    times[0].append(end_time-start_time)
    #pop
    for j in range(len(list_list[i])-1):
        temp.push(list_list[i][j])
    start_time=time.time_ns()
    temp.pop()
    end_time=time.time_ns()
    times[1].append(end_time-start_time)


x=range(10,len(times[0])+10)
fig, ax = plt.subplots(nrows=1,ncols=1)
plt.xlabel("wielkość tabeli")
plt.ylabel("czas(ns)")
ax.plot(x,times[0],label="Push")
ax.plot(x,times[1],label="Pop")
ax.legend()
plt.show()
#zad 1

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
    def get_children(self,index,stop=None):
        if stop==None:
            stop=len(self._A)-1
        if (2*index)+1>stop:
            return [None,None]
        if (2*index)+2>stop:
            return [(2*index)+1,None]
        return [(2*index)+1,(2*index)+2]
    def get_parent(self,index):
        if index==0:
            raise ValueError("root has no parent")
        if index%2==0:
            return floor(index/2)-1
        elif index%2==1:
            return floor(index/2) 

#zad4

#zad5
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Może być operatorem (+, -, *, /), zmienną (x) lub liczbą
        self.left = left
        self.right = right

def diff(node, var):
    
    #Stała lub inna zmienna: d/dx(c) = 0, d/dx(y) = 0
    if not node.left and not node.right:
        return Node("1") if node.value == var else Node("0")

    #Suma i Różnica: (f +/- g)' = f' +/- g'
    if node.value in ["+", "-"]:
        return Node(node.value, diff(node.left, var), diff(node.right, var))

    #Iloczyn: (f * g)' = f' * g + f * g'
    if node.value == "*":
        left_side = Node("*", diff(node.left, var), node.right)
        right_side = Node("*", node.left, diff(node.right, var))
        return Node("+", left_side, right_side)

    #Iloraz: (f / g)' = (f' * g - f * g') / g^2
    if node.value == "/":
        numerator = Node("-", 
                         Node("*", diff(node.left, var), node.right),
                         Node("*", node.left, diff(node.right, var)))
        denominator = Node("^", node.right, Node("2"))
        return Node("/", numerator, denominator)

    return Node("Błąd: Nieobsługiwany operator")

#       +
#      / \
#     /   5
#    / \
#   +   x
#  / \
# 3   x
node_3 = Node("3")
node_x1 = Node("x")
node_5 = Node("5")
node_x2=Node("x")
node_plus=Node("+",node_3,node_x1)
node_div=Node("/",node_plus,node_x2)
root=Node("+",node_5,node_div)

derivative_tree = diff(root, "x")

def to_string(node):
    if not node.left and not node.right:
        return node.value
    return f"({to_string(node.left)} {node.value} {to_string(node.right)})"

print(f"Oryginalne wyrażenie: {to_string(root)}")
print(f"Surowa pochodna: {to_string(derivative_tree)}")
#zad5