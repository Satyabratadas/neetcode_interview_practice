class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                continue
            for j in range(i+1, n):
                b = nums[j]
                if j > i+1 and b == nums[j-1]:
                    continue
                l, r = j+1, n-1

                while l < r:
                    total = a + b + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append([a, b, nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return res