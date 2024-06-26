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
        m = ili(n)
        sum_m = 0
        con_even = 0
        con_odd = 0
        for i in m:
            if i % 2 == 0:
                con_even += 1
            else:
                con_odd += 1
            sum_m += i
        for i in range(k):
            p, q = ili(2)
            if p == 0:
                sum_m += con_even * q
                if q % 2 != 0:
                    con_odd += con_even
                    con_even = 0
            else:
                sum_m += con_odd * q
                if q % 2 == 1:
                    con_even += con_odd
                    con_odd = 0
            print(sum_m)


if __name__ == "__main__":  # 12 4 6
    main()
