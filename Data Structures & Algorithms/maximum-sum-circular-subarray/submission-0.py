class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        curMax = curMin = total = 0
        for n in nums:
            curMax = max(curMax + n, n)
            globMax = max(globMax, curMax)
            curMin = min(curMin + n, n)
            globMin = min(curMin, globMin)
            total += n
        return max(globMax, total - globMin) if globMax > 0 else globMax