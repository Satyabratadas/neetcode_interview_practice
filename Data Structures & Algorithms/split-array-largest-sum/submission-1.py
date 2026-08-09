class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        result = r

        while l <= r:
            m = l + (r - l) // 2
            if self.canSplit(m, nums, k):
                result = m
                r = m - 1
            else:
                l = m + 1
        return result

    def canSplit(self, largest, arr, target):
        subArr = 1
        current = 0
        for n in arr:
            current += n
            if current > largest:
                subArr += 1
                current = n
        return subArr <= target


        