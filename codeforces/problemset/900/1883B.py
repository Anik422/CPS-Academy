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
        n, k = ili(2)
        s = si()
        if k == 0 and s == s[::-1]:
            print("YES")
        elif n - k == 1:
            print("YES")
        else: 
            con = Counter(s)
            if len(con.keys()) == n:
                print("NO")
            else:
                odd = 0
                oddSum = 0
                even = 0
                for i in con.keys():
                    if con[i] % 2 != 0 and k > 0:
                        con[i] -= 1
                        k -= 1
                    elif con[i] % 2 != 0:
                        odd += 1
                        oddSum += con[i]
                    else:
                        even += con[i]
                if 1 >= odd and k == 0:
                    print("YES")
                elif odd > 1 and k == 0:
                    print("NO")
                elif k != 0:
                    print("YES")
                
               
                
                


if __name__ == "__main__":  # 12 4 6
    main()
