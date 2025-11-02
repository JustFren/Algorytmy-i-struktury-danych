import os

s=[1,2,3,4,5]
#zad1
def max_el(S,i,max):
    if i==len(S):
        return max
    if S[i]>max:
        max=S[i]
    return max_el(S,i+1,max)    
#print(max_el(s,0,0))
#zad1

#zad3
def minmax_el(S,i,ext):
    #ext=[min,max]
    if i==len(S):
        return ext
    if S[i]>ext[1]:
        ext[1]=S[i]
    if S[i]<ext[0]:
        ext[0]=S[i]
    return minmax_el(S,i+1,ext)
#print(minmax_el(s,0,[max_el(s,0,0),0]))
#zad3

#zad4
def mult(m,n):
    if n==1:
        return m
    return m+mult(m,n-1)
#print(mult(6,7))
#zad4

#zad5
def czy_palindrom(S,n):
    if S[n]!=S[len(S)-1-n]:
        return False
    if n==len(S)//2:
        return True
    return czy_palindrom(S,n+1)
#print(czy_palindrom("(){}",0))    
#zad5

#zad6
def get_file(path,filename):
    path=os.getcwd()+path[1:]
    dir_list=os.listdir(path)
    output=[]
    def _get_file(path,filename,dir_list,output):
        temp_path=path
        if os.path.isfile(temp_path):
                #print(temp_path)
                out=""
                for i in range(len(filename)):
                    out+=temp_path[-(i+1)]
                if out[::-1]==filename:
                    output.append(temp_path)
                return
        dir_list=os.listdir(path)
        for dir in dir_list:
            temp_path=path+r'\\'+f"{dir}"
            _get_file(path+"\\"+f"{dir}",filename,dir_list,output)
        return output    
    return _get_file(path,filename,dir_list,output)  

print(get_file(".\\lista_2\\ex_folder","plik1"))
#zad6
