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
        m = ili(n)
        ans = 0
        list_3 = []
        i = 0
        while i < n -2:
            if m[i:i+3] not in list_3:
                list_3.append(m[i:i+3])
            i += 1
        for i, item in enumerate(list_3):
            for j in list_3[i+1:]:
                if item[0] != j[0] and item[1] == j[1] and item[2] == j[2]:
                    ans += 1
                    break
                if item[0] == j[0] and item[1] != j[1] and item[2] == j[2]:
                    ans += 1
                    break
                if item[0] == j[0] and item[1] == j[1] and item[2] != j[2]:
                    ans += 1
                    break
        print(ans)
        
            


if __name__ == "__main__":  # 12 4 6
    main()
