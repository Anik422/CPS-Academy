n, m, x = map(int, input().split())
num1 = list(map(int, input().split()))[:n]
num2 = list(map(int, input().split()))[:n]

num1.sort()
num2.sort()

defs = float("inf")

ind1 = 0
ind2 = 0

start = 0
end = m - 1

while start < n - 1 and end >= 0:
    sumT = num1[start] + num2[end]
    if abs(sumT - x) < defs:
        ind1 = start
        ind2 = end
        defs = sumT
    if sumT > x:
        end -= 1
    else: 
        start += 1
print(f"({num1[ind1]}, {num2[ind2]}), sum = {num1[ind1] + num2[ind2]}")
