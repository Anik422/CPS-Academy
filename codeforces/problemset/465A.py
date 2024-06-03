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
    n = ii()
    s = si()
    m = int(s, 2)
    m += 1
    m2 = format(m, "b")
    m2 = "0" * (n - len(m2)) + m2
    if len(m2) == n:
        print(m2.count("1"))
    else:
        print(s.count("1"))
if __name__ == "__main__":
    main()
