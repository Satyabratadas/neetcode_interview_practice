class Solution:
    ## Using two pointer space O(1)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        left_max, right_max = height[l], height[r]
        res = 0
        if n == 0:
            return 0
        while l < r:
            if left_max < right_max:
                l += 1
                diff = left_max - height[l]
                if diff > 0:
                    res += diff
                left_max = max(left_max, height[l])
            else:
                r -= 1
                diff = right_max - height[r]
                if diff > 0:
                    res += diff
                right_max = max(right_max, height[r])
        return res

