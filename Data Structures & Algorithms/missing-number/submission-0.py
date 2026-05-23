class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        exp_sum = (n * (n+1)) // 2

        print(exp_sum, total)

        return exp_sum - total