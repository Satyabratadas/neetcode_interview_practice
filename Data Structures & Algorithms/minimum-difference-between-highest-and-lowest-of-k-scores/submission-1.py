class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        result = float("inf")
        left = 0
        for right in range(k - 1, len(nums)):
            result = min(result, (nums[right] - nums[left]))
            left += 1
        return result