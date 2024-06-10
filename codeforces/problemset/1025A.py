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
    if n == 1:
        print('YES')
        return
    con = Counter(s)
    con1 = 0
    cons = 0
    for i in con:
        if con[i] == 1:
            con1 += 1
        else:
            cons += 1

    if cons != 0:
        print('YES')
    else:
        print('NO')
        


if __name__ == "__main__":  # 12 4 6
    main()
