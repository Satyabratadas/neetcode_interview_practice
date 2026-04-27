class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c_map = {}
        total = len(nums) // 2
        for num in nums:
            c_map[num] = c_map.get(num, 0) + 1
        for key, value in c_map.items():
            if value > total:
                return key
