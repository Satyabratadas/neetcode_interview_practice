class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_arr = []
        left = 0
        right = len(nums) - 1
        for i in range (0, len(nums)):
            nums[i] = nums[i] ** 2
        while left <= right:
            if nums[left] > nums[right]:
                sqr_arr.append(nums[left])
                left += 1
            else:
                sqr_arr.append(nums[right])
                right -= 1
        return sqr_arr[::-1]