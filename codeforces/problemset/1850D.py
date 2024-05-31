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
        m = ili(n)
        if n == 1:
            print(0)
            continue
        m.sort()
        c = 1
        ans = []
        for i in range(n - 1):
            if abs(m[i] - m[i + 1]) <= k:
                c += 1
            else:
                ans.append(c)
                c = 1
        
        ans.append(c)

        print(n - max(ans))


if __name__ == "__main__":  # 12 4 6
    main()
