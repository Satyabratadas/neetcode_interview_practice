class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current = 0
        res = 0
        presum_dict = {0:1}

        for num in nums:
            current += num
            diff = current - k
            res += presum_dict.get(diff, 0)
            presum_dict[current] = presum_dict.get(current, 0) + 1
        
        return res



        