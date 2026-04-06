class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        sub_sum = {0:1}
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            res += sub_sum.get(diff,0)
            sub_sum[cur_sum] = 1 + sub_sum.get(cur_sum, 0)
        return res