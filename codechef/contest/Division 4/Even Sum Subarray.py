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

def largest_even_sum_subarray(arr):
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return len(arr)
    
    odd_positions = [i for i, num in enumerate(arr) if num % 2 != 0]
    
    if len(odd_positions) == 0:
        return 0  
    
 
    first_odd_position = odd_positions[0]
    last_odd_position = odd_positions[-1]
    
   
    remove_prefix_length = first_odd_position + 1
    remove_suffix_length = len(arr) - last_odd_position
    
    return max(len(arr) - remove_prefix_length, len(arr) - remove_suffix_length)


def main():
    t = ii()
    for _ in range(t):
        n = ii()
        m = ili(n)
        print(largest_even_sum_subarray(m))


if __name__ == "__main__":  # 12 4 6
    main()
