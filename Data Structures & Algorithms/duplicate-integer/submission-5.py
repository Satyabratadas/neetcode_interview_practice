class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = set(nums)
        if len(count_map) == len(nums):
            return False
        else:
            return True
