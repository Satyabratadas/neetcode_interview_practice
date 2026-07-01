class Solution:

    def binarySearch(self, arr, start, end, k):
        m = (start + end) // 2
        if start > end:
            return -1
        if arr[m] == k:
            return m
        elif arr[m] < k:
            return self.binarySearch(arr, m + 1, end, k)
        return self.binarySearch(arr, start, m - 1, k)

        
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
