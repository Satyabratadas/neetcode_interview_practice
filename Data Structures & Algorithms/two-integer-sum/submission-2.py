class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in check_map:
                return [check_map[diff], i]
            check_map[num] = i
            