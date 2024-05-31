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
        n = ii()
        m1 = ili()
        m2 = ili()
        ok = True
        ans = 0
        for i in range(n):
            if ok == True and ((m1[i] <= m2[-1] and m2[-1] <= m2[i]) or (m1[i] >= m2[-1] and m2[-1] >= m2[i])):
                ans += 1
                ok = False
            if m2[i] != m1[i]:
                ans += abs(m2[i] - m1[i])
        if ok:
            val = 0
            mn = float("inf")
            for i in range(n):
                if abs(m1[i] - m2[-1]) < mn:
                    mn = abs(m1[i] - m2[-1])
                    val = m1[i]
                if abs(m2[i] - m2[-1]) < mn:
                    mn = abs(m2[i] - m2[-1])
                    val = m2[i]
            ans += (abs(m2[-1] - val)) + 1
        print(ans)


if __name__ == "__main__":  # 12 4 6
    main()
