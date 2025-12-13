import matplotlib.pyplot as plt
import numpy as np
import time
import random
#współczynniki są podawane w konwencji ( wsp przy x^0 , wsp przy x^1 , ... ,wsp przy x^n)
def zad1_1(val,coeff):
    """coeff to lista współczynników wielomianu"""
    sum=0
    for i in range(len(coeff)):
        temp=val
        for j in range(i):    
            temp*=val
        sum+=temp*coeff[i]
    return sum        

def zad1_2(val,coeff):
    def szybka_potęga(x,n):
        s=""
        while n!=0:
            if n%2 == 1:
                s+="1"
            else:
                s+="0"
            n=n//2       
        s=s[::-1]    
        #algorytm wzięty z wikipedii
        w=1
        for c in s:
            if c == "0":
                w*=w
            if c == "1":
                w=w*w*x
        #algorytm wzięty z wikipedii
        return w

    sum=0
    for i in range(len(coeff)):
        temp=szybka_potęga(val,int(i))
        sum+=val*coeff[i]
    return sum    

def zad1_3(val,coeff):
    if coeff==1:
        return coeff*val
    coeff=coeff[::-1]
    sum=coeff[0]
    

    for i in range(1,len(coeff)):
        sum=val*sum+coeff[i]
    return sum    

def sprawdzenie_poprawnosci_zad1(val,coeff):
    print(zad1_1(val,coeff))
    print(zad1_2(val,coeff))
    print(zad1_3(val,coeff))

def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

def example2(S):
    """Return the sum of the elements with even index in sequence S.
    """
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total

def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total

def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex
    sums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count    

def zad2_test():
    x=range(1,500,10)
    A=[random.choices(range(50),k=i) for i in range(1,500,10)]
    B=[random.choices(range(50),k=i) for i in range(1,500,10)]
    fig, ax = plt.subplots(2,2)
    #plt.yscale("log")
    #plt.xscale("log")
    wyniki=[[],[],[],[]]
    funkcje=[example1,example2,example3]
    for rozklad in A:
        for i in range(3):
            t_begin=time.time_ns()
            funkcje[i](rozklad)
            t_end=time.time_ns()
            wyniki[i].append(t_end-t_begin)
       
    for j in range(len(A)):
        t_begin=time.time_ns()
        example4(A[j],B[j])
        t_end=time.time_ns()
        wyniki[3].append(t_end-t_begin)

    ax0=wyniki[0]
    print(wyniki[0])
    print(wyniki[1])
    print(wyniki[2])
    ax1=wyniki[1]
    ax2=wyniki[2]
    ax3=wyniki[3]

    ax[0,0].plot(x ,ax0, label="example1")
    ax[0,0].set_xlabel("example1")
    ax[0,1].plot(x ,ax1, label="example2")
    ax[0,1].set_xlabel("example2")
    ax[1,0].plot(x ,ax2, label="example3")
    ax[1,0].set_xlabel("example3")
    ax[1,1].plot(x ,ax3, label="example4")
    ax[1,1].set_xlabel("example4")
    #ax.legend()
    plt.show()


def zad3():
    x=range(1,10000,1)
    fig, ax = plt.subplots()
    A=[random.choices(range(50),k=i) for i in range(1,10000,1)]
    wyniki=[[],[]]
    f=lambda n : 6*n*np.log(n)
    for rozklad in A:
        t_begin=time.time_ns()
        sorted(rozklad)
        t_end=time.time_ns()
        wyniki[0].append(t_end-t_begin)
        wyniki[1].append(f(len(rozklad)))
    ax1=wyniki[0]
    ax2=wyniki[1]
    ax.plot(x,ax1,label="sorted")
    ax.plot(x,ax2,label="6 n log n")
    ax.legend()
    plt.show()


#sprawdzenie_poprawnosci_zad1(1,(1,2,1))
#zad2_test()
zad3()