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
    con = 0
    st = 1
    en = n + 1
    while st < en:
        b = mt.sqrt((en ** 2) - (st ** 2))
        if b == int(b) and b <= n:
            con += 1
        if b < n:
            st += 1
        else:
            en -= 1
            
            
    # c = mt.sqrt((i ** 2 + j ** 2))
    # if c == int(c) and c <= n and c != i and c != j:
    #     con += 1
    # elif c > n:
    #     break
    print(con)


if __name__ == "__main__":  # 12 4 6
    main()
