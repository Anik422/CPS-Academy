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
        n, k = ili(2)
        m1 = [(int(x),i) for i,x in enumerate(input().split())]
        m2 = ili(n)
        m1.sort()
        m2.sort()
        ans = [0] * n
        for i in range(n):
            ans[m1[i][1]] = m2[i]
        print(*ans)

if __name__ == "__main__":  # 12 4 6
    main()
