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
    ans = 0
    con = 0
    for i in range(n - 1):
        if m[i] != m[i + 1]:
            con += 1
        else:
            con += 1
            ans = max(ans, con)
            con = 0
    ans = max(ans, con + 1)
    print(ans)


if __name__ == "__main__":  # 12 4 6
    main()
