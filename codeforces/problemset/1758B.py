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
        if n % 2 != 0:
            m = [n] * n
            print(*m)
        else:
            bi1 = format(n, "b")

            bi2 = "".join(["0" if bi1[i] == "1" else "1" for i in range(len(bi1))])
            ds2 = int(bi2, 2)
            m = [n] * n
            m[-1] = ds2
            print("XOR = ", ds2 ^ n)
            print(*m)


if __name__ == "__main__":  # 12 4 6
    main()
