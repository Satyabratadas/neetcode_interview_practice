class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            if self.canSplit(mid, nums, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def canSplit(self, largest, arr, target):
        subArrCnt = 1
        current = 0
        for n in arr:
            current += n
            if current > largest:
                subArrCnt += 1
                current = n
        return subArrCnt <= target