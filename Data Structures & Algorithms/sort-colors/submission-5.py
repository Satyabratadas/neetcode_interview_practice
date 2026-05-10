class Solution:

    ## Using three pointer dutch national flag algo
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                self.swap(nums, l, i)
                l += 1
                i += 1
            elif nums[i] == 2:
                self.swap(nums, i, r)
                r -= 1
            else:
                i += 1
        return nums

        