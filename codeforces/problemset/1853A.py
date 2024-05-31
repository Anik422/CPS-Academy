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
    for _ in range(ii()):
        n = ii()
        m = ili(n)
        sort_m = sorted(m)
        if m != sort_m:
            print(0)
        else:
            mn = float("inf")
            for i in range(n-1):
                mn = min(mn, m[i+1] - m[i])
            print((mn // 2) + 1)
            


if __name__ == "__main__":  # 12 4 6
    main()
