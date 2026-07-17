class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                res = i
        return res