class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0

        if not nums:
            return 0
        for n in nums:
            if curr < 0:
                curr = 0

            curr += n
            if maxSum < curr:
                maxSum = curr
        return maxSum
