def solve(nums, n):
    for i in range(n - 1, -1, -1):
        st = 0
        en = i - 1
        while st < en:
            sumT = nums[st] + nums[en]
            if sumT == nums[i]:
                print(f"{nums[i]}, {nums[st]}, {nums[en]}")
            if sumT > nums[i]:
                en -= 1
            else:
                st += 1


n = int(input())
m = list(map(int, input().split()))
m.sort()
solve(m, n)
