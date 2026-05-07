class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c_map = {}
        target = len(nums) // 3
        res = []
        for num in nums:
            c_map[num] = c_map.get(num, 0) + 1
        
        for key, value in c_map.items():
            if value > target:
                res.append(key)
        return res