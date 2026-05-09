class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = len(nums) // 3
        c_map = {}
        res = []
        for num in nums:
            c_map[num] = c_map.get(num, 0) + 1
        for key, value in c_map.items():
            if value > check:
                res.append(key)
        return res