class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        start, end = nums[0], nums[n - 1]
        if start <= end:
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    return False
            return True
        else:
            for i in range(1, n):
                if nums[i - 1] < nums[i]:
                    return False
            return True

        

