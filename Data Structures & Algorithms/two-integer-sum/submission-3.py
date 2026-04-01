from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in count:
                return [count[diff], i]
            else:
                count[num] = i