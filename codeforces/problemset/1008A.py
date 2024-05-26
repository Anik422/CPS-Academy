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
    s = si()
    v = {"a": True, "e": True, "i": True, "o": True, "u": True, "n": True}
    vow = v.get(s[0], False)
    if len(s) == 1:
        if vow:
            print("YES")
        else:
            print("NO")
    elif not v.get(s[-1], False):
        print("NO")
    else:
        ok = True
        for i in range(1, len(s)):
            if s[i] == "n" and s[i - 1] != "n" and not v.get(s[i - 1], False):
                ok = False
                break
            elif not vow and v.get(s[i], False):
                vow = True
                continue
            elif vow and not v.get(s[i], False):
                vow = False
                continue
            elif vow and v.get(s[i], False):
                vow = True
                continue
            else:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":  # 12 4 6
    main()
