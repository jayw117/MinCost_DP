from timeit import timeit
# Problem : Given two areas to work (New York and San Francisco) for n weeks. One must find the minimum cost between these two areas. However
# if one was to move to the other area there is a moving cost, M that must be added to the cost.
# This was solved using dynamic programming as well as brute force and the timeit function to show the time it takes to run.
totals = []
comb = []
ny = []
sf = []
n=5
M=15
N=[32, 34, 38, 23, 44]
S=[50, 25, 42, 10, 13]
arr = [None] * n

def bottomup():         # bottom up approach
    for i in range(len(N)):
        ny.append(0)
    for i in range(len(S)):
        sf.append(0)
    for i in range(0, n):
        
        ny[i] = N[i] + min(sf[i-1] + M, ny[i-1])
        sf[i] = S[i] + min(ny[i-1] + M, sf[i-1])
        
    return(min(ny[i],sf[i]))
    
    
NYcache = {0:0} # Cache that stores values for optNY
SFcache = {0:0} # Cache that stores values for optSF 

# Top Down Approach
def optNY(i):  #lowest possible cost of i weeks (n) if ith week is in NY
    
    if i in NYcache:
        return NYcache[i]
    
    else:
          
        NYcache[i] = N[i-1] + min(optSF(i-1) + M, optNY(i-1))
        return NYcache[i]
     
def optSF(i): #lowest possible cost of i weeks (n) if ith week is in SF
    
    if i in SFcache:
        return SFcache[i]
    else:
        
        SFcache[i] = S[i-1] + min(optNY(i-1) + M, optSF(i-1))
        return SFcache[i]
    
optNY(n)
optSF(n)

def topDown():
    return("TOPDOWN", min(optNY(n), optSF(n)))
    

# Brute Force 

def bruteforce(n, bs = ''): #credit to GeeksForGeek for the code that makes every combination of binary numbers
   
    if len(bs) == n:
        
        
        comb.append(bs)
    else:
        bruteforce(n, bs + '0')
        bruteforce(n, bs + '1')
        
        
print("BOTTOM UP", bottomup())
bruteforce(n)
print( topDown())


def brute():
    total = 0
    for i in comb:
        if i[0] == "0":
            total += N[0]
        if i[0] == "1":
            total += S[0]
        for j in range(1,len(i)):
                               
            if i[j] == "0":
                
                    
                if i[j-1] == "1" and i[j] == "0":
                    total += N[j] + M
                else:
                    total += N[j]
            
            if i[j] == "1":
                
                if i[j-1] == "0" and i[j] == "1":
                    total += S[j] + M
                else:
                    total += S[j]
            
            
        totals.append(total)
        total = 0
    l = min(totals)
    return l
 
print("BRUTE", brute())

def wrapper(func, *args): #wraps a function to allow the timeit function to use it 
    def wrapped():          #credit to Brandon Chupp for deciphering this
        return func(*args)
    return wrapped
    
x = wrapper(bottomup) #passes our NewSan function through the wrapper
print("BottomUp: size:", n, "time:", timeit(x, number = 1000)/1000)    #average runtime of 10,000 trials of size n


v = wrapper(topDown)
c = wrapper(brute)
b = wrapper(bruteforce, n)


print("TopDown: size:", n, "time:",  (timeit(v, number = 100)/100))

print("Brute: size:", n, "time:",  (timeit(c, number = 5)/5) + (timeit(b, number = 5)/5))

