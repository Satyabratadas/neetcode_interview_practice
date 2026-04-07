class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        sum_sub = {0 : 1}
        for num in nums:
            current_sum += num
            diff = current_sum - k
            result += sum_sub.get(diff, 0)
            sum_sub[current_sum] = 1 + sum_sub.get(current_sum, 0)
        return result