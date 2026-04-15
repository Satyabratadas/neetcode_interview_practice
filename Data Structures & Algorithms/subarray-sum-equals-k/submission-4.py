class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_arr = []
        pre_sum = 0
        sub_count = {0:1}
        res = 0

        for num in nums:
            pre_sum += num
            pre_arr.append(pre_sum)

        for n in pre_arr:
            diff = n - k
            res += sub_count.get(diff, 0)
            sub_count[n] = 1 + sub_count.get(n, 0)
        return res



        