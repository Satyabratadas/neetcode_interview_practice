class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum, res = 0, 0
        pre_sum = {0:1}
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += pre_sum.get(diff, 0)
            pre_sum[curr_sum] = 1 + pre_sum.get(curr_sum, 0)
        return res



        