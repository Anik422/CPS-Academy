from collections import Counter
import math as mt


def si():
    return input()


def ii():
    return int(input())


def fi():
    return float(input())


def ili(n=None):
    if n:
        return list(map(int, input().split()))[:n]
    return list(map(int, input().split()))


def fli(n=None):
    if n:
        return list(map(float, input().split()))[:n]
    return list(map(float, input().split()))


def sli(n=None):
    if n:
        return list(map(str, input().split()))[:n]
    return list(map(str, input().split()))


def minInd(m: list):
    mn = m[0]
    ind = 0
    l = len(m)
    for i in range(1, l):
        if m[i] < mn:
            mn = m[i]
            ind = i
    return [mn, ind]


def main():
  
    n, k = ili(2)
    m = ili(n)
    m = list(set(m))
    m.sort()
    pre = 0
    m += [0] * (k-len(m))
    for i in range(k):
        if m[i] != 0:
            print(m[i]-pre)
            pre = m[i]
        else:
            print(m[i])
      
       
            
            
        
   
        
            
        
        

if __name__ == "__main__":  # 12 4 6
    main()
