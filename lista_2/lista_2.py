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

#zad2
#zad2

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
print(os.listdir("./lista_2/ex_folder"))
#zad6
