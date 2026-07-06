class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    
    def binarySearch(self, arr, k, leftBias):
        l, r = 0, len(arr) - 1
        i = -1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] < k:
                l = m + 1
            elif arr[m] > k:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
