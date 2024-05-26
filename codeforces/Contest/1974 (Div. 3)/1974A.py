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
    t = ii()
    for _ in range(t):
        n, k = ili(2)
        if k == 0 and n == 0:
            print(0)
        elif k == 0 and n != 0:
            print(mt.ceil(n / 15))
        elif n == 0 and k != 0:
            print(mt.ceil(k / 2))
        elif k == 1:
            n -= 11
            if n < 0:
                print(1)
            else:
                print(mt.ceil(n / 15) + 1)
        elif k % 2 == 1:
            kdis = mt.ceil(k / 2)
            n -= ((kdis - 1) * 7)
            n -= 11
            if n < 0:
                print(kdis)
            else:
                print(kdis + mt.ceil(n / 15))
        else:
            kdis = mt.ceil(k / 2)
            n -= (kdis * 7)
            if n < 0:
                print(kdis)
            else:
                print(kdis + mt.ceil(n / 15))
            


if __name__ == "__main__":  # 12 4 6
    main()
