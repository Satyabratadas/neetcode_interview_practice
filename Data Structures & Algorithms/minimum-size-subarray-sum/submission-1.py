class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr = 0, 0
        size = float('inf')

        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                size = min(r - l + 1, size)
                curr -= nums[l]
                l += 1
        return 0 if size == float('inf') else size