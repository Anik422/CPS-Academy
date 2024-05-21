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
        m = ili()
        ans = []
        st = 0
        en = n - 1
        while st < en:
            ans.append(m[st])
            ans.append(m[en])
            st += 1
            en -= 1
        if n % 2 == 1:
            ans.append(m[n // 2])

        print(*ans)


if __name__ == "__main__":  # 12 4 6
    main()
