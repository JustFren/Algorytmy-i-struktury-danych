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

class graph():
    def __init__(self):
        self.vertex={}
    def __str__(self):
        return str(self.vertex)
    def __contains__(self,key):
        if type(key)!=type(""):
            key=str(key)
        return key in [*self.vertex.keys()]
    def add_vertex(self,key):
        self.vertex[str(key)]=[]
    def add_vertex_from_list(self,list):
        for item in list:
            self.vertex[str(item[0])]=item[1]    
    def add_edge(self,from_vert,to_vert,weight=1):
        from_vert=str(from_vert)
        to_vert=str(to_vert)
        if from_vert not in self.vertex:
            self.vertex[from_vert]=[]
        if to_vert not in self.vertex:
            self.vertex[to_vert]=[]    
        self.vertex[from_vert].append([str(to_vert),weight])
    def add_edge_from_list(self,list):
        for item in list:
            from_vert=item[0]
            to_vert=item[1]
            try:
                weight=item[2]
            except:
                weight=1    
            self.add_edge(from_vert,to_vert,weight)
    def get_vertices(self):
        return [*self.vertex]
    def get_edges(self):
        out=[]
        for item in self.vertex:
            if self.vertex[str(item)]==[]:
                continue
            for edge in self.vertex[str(item)]:
                out.append([item,edge[0]])
        return out    
    def get_neighbors(self,vert_key):
        if type(vert_key) != type(""):
            vert_key=str(vert_key) 
        out=[]
        for edge in self.vertex[vert_key]:
            out.append(edge)
        return out    
    def save_graph(self):
        plik=open("./lista_7/graph.txt","w")
        out="digraph G{\n"
        for item in self.get_vertices():
            temp=[]
            for neighbor in self.get_neighbors(item):         
                out+=f"\"{str(item)}\"->\"{str(neighbor[0])}\";\n"
        out+="}"        
        plik.write(out)
    
    def dfs(self, start_node):
        s=stack()
        order=[]
        s.push(str(start_node))
        while s.is_empty()!=1:
            temp=self.get_neighbors(s.top())
            temp=[it[0] for it in temp]
            #print(temp)
            if s.top() in order:
                s.pop()
            else:
                order.append(s.pop())
                for item in temp:
                    s.push(item)
        return order
    def bfs(self,start_node):
        q=Queue()
        order=[]
        q.enqueue(str(start_node))
        while q.is_empty()!=1:
            temp=self.get_neighbors(q.first())
            temp=[it[0] for it in temp]
            if q.first() in order:
                q.dequeue()
            else:
                order.append(q.dequeue())
                for item in temp:
                    q.enqueue(item)
        return order    
    def shortest_path_bfs(self,start_node,end_node):
        paths={}
        order=[]
        for item in self.get_vertices():
            paths[item]=[]
        q=Queue()
        q.enqueue(str(start_node))
        paths[str(start_node)]=[str(start_node)]
        while q.is_empty()!=1:
            temp=self.get_neighbors(q.first())
            temp=[it[0] for it in temp]
            for item in temp:
                if paths[item]==[]:
                    paths[item].extend(paths[q.first()])
                    paths[item].append(item)
                elif paths[item]!=[]:
                    temp1=paths[q.first()][:]
                    temp1.append(item)
                    if len(paths[item])>len(temp1):
                        paths[item]=temp1

            if q.first() in order:
                q.dequeue()
            else:
                order.append(q.dequeue())
                for item in temp:
                    q.enqueue(item)
        return paths[str(end_node)]                  
        
#zad1
#g=graph()
#g.add_edge(1,2)
#g.add_edge(1,3)
#g.add_edge(3,5)
#g.add_edge(5,6)
#g.add_edge(2,4)
#g.add_edge(2,6)
#print(g.get_neighbors(1))

#zad 2
#g.save_graph()
#zad 3
#print(g.dfs(1))
#print(g.bfs(1))
#zad 4
#graf musi być acykliczny
#print(g.dfs(1))
#to dfs nie zwraca uwagi na cykle więc wynik jest posortowany topologicznie

#zad 5
#print(g.shortest_path_bfs(1,6))

#zad 6
#zaczynamy od stanu [3 misjonarze ,3 kanibale ,True] gdzie True oznacza że przy tej stronie jest łódka
#
valid_states=[]
g=graph()
begin=[3,3,1]
states=[]
s=[]
states.append([begin,[]])
changes=[(-1,-1,-1),(1,1,1),(-2,0,-1),(2,0,1),(0,-2,-1),(0,2,1)\
         ,(-1,0,-1),(1,0,1),(0,-1,-1),(0,1,1)]

def is_change_elegible(state,change):
    if state[0]+change[0]>3 or state[0]+change[0]<0:
        return False
    if state[1]+change[1]>3 or state[1]+change[1]<0:
        return False
    if state[2]==1 and change[2]==1:
        return False
    if state[2]==0 and change[2]==-1:
        return False
    if state[0]+change[0]<state[1]+change[1]:
        if state[0]+change[0]==0:
            pass
        else:return False
    if state[0]+change[0]==2 and state[1]+change[1]==1:
        return False
    if state[0]+change[0]==1 and state[1]+change[1]==0:
        return False
    if state[0]+change[0]==2 and state[1]+change[1]==0:
        return False
    return True

#for change in changes:
#        if is_change_elegible(begin,change):
#            print(f"[{begin[0]+change[0]},{begin[1]+change[1]},{begin[2]+change[2]}]")
#quit()

q=Queue()
q.enqueue([begin,[]])
def v_sum(v1,v2):
    out=[0 for i in v1]
    for i in range(len(v1)):
        out[i]=v1[i]+v2[i]
    return out    
counter=0
edges=[]
while q.is_empty()!=1:
    temp=[]
    for change in changes:
        if is_change_elegible(q.first()[0],change):
            t=q.first()[:]
            t=t[1][:]
            t.append(change)
            if len(t)>=2:
                if v_sum(change,t[-2])==[0,0,0]:
                    continue
            temp.append([v_sum(q.first()[0],change),t])
            if [q.first()[0],v_sum(q.first()[0],change)] not in edges:
                edges.append([q.first()[0],v_sum(q.first()[0],change)])
                g.add_edge(q.first()[0],v_sum(q.first()[0],change))
    if q.first()!=[begin,[]]:states.append(q.dequeue())
    else: q.dequeue()
    for item in temp:
        if item[1] not in s and len(item[1])<20:
            s.append(item[1])
            q.enqueue(item)
         
g.save_graph()

print(g.shortest_path_bfs(begin,[0,0,0]))




