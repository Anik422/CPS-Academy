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
    m = ili()
    ans = 0
    st = 0
    en = n - 1
    a1 = 0
    b1 = 0
    while st <= en:
        if b1 < a1:
            b1 += m[en]
            en -= 1
        else:
            a1 += m[st]
            st += 1
        if a1 == b1:
            ans = max(ans, b1)
       
   
    print(ans)


if __name__ == "__main__":  # 12 4 6
    main()
