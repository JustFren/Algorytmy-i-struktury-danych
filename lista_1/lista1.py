import matplotlib


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

#def sprawdzenie_poprawnosci_zad1(val,coeff):
#    print(zad1_1(val,coeff))
#    print(zad1_2(val,coeff))
#    print(zad1_3(val,coeff))

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

