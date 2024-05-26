n, x = map(int, input().split())
m = list(map(int, input().split()))[:n]
m.sort()
start = 0
end = n - 1
defr = float("inf")
ind1 = 0
ind2 = 0
while start < end:
    sumT = m[start] + m[end]
    if abs(x - sumT) < defr:
        ind1 = start
        ind2 = end
        defr = abs(x - sumT)
    if sumT > x:
        end -= 1
    else:
        start += 1
print(
    "(",
    m[ind1],
    ",",
    m[ind2],
    ")", "=",
    m[ind1] + m[ind2]
)
