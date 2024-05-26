n, x = map(int, input().split())
m = list(map(int, input().split()))[:n]
m.sort()
start = 0
end = n - 1
while start < end:
    if m[start] + m[end] == x:
        print("YES")
        break
    elif m[start] + m[end] < x:
        start += 1
    elif m[start] + m[end] > x:
        end -= 1
else:
    print("NO")