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
    s = si()
  
    s = sorted(s)
    ans = ord(s[0]) - 96
    pre = ord(s[0]) - 96
    k -= 1
    for i in s[1:]:
        if (pre + 1) < (ord(i) - 96) and k > 0:
            pre = ord(i) - 96
            ans += (ord(i) - 96)
            k -= 1
    if k == 0:
        print(ans)
    else:
        print(-1)
    



if __name__ == "__main__":  # 12 4 6
    main()
