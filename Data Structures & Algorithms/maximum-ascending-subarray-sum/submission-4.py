class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            curr += nums[i]
            if nums[i] <= nums[i - 1]:
                curr = nums[i]
            result = max(curr, result)
        return result
        