def solve(nums, n, x):
    for i in range(n):
        start = i + 1
        end = n - 1
        while start < end:
            sumT = nums[i] + nums[start] + nums[end]
            if sumT == x:
                print(nums[i], nums[start], nums[end])
            if sumT > x:
                end -= 1
            else:
                start += 1


n, x = map(int, input().split())
num = list(map(int, input().split()))[:n]
num.sort()
solve(num, n, x)
