class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        length = len(arr)
        if len(arr) % 2 == 0:
            return (arr[(length // 2) - 1] + arr[length // 2]) / 2
        else:
            return (arr[length // 2])