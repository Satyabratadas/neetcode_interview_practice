class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        pre_sum = 0

        for num in nums:
            total_sum += num

        for i, num in enumerate(nums):
            right_sum = total_sum - pre_sum - num
            if right_sum == pre_sum:
                return i
            pre_sum += num
        return -1
        