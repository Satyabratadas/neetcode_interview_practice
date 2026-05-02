## Using Bubble Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        did_swap = 0
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    did_swap = 1
            if did_swap == 0:
                break
        return nums