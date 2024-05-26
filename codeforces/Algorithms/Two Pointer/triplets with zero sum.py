def solve(nums, n):
    for i in range(n):
        unordered_set = set()
        for j in range(i + 1, n):
            x = -(nums[i] + nums[j])
            if x  in unordered_set:
                print(f"({x}, {nums[i]}, {nums[j]})")
            else:
                unordered_set.add(nums[j])
                

n = int(input())
num = list(map(int, input().split()))[:n]
num.sort()
solve(num, n)