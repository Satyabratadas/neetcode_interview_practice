class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        arr = []

        for i in range(len(nums)):
            arr.insert(0, sorted_nums.pop())
            if nums == arr + sorted_nums:
                return True
        return False