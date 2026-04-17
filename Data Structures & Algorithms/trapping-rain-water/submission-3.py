class Solution:
    ## Using two pointer space O(1)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        count = 0
        l, r = 0, n - 1
        l_max, r_max = height[l], height[r]

        if n == 0:
            return 0

        while l < r:
            if l_max < r_max:
                l += 1
                diff = l_max - height[l]
                if diff > 0:
                    count += diff
                l_max = max(l_max, height[l])
            else:
                r -= 1
                diff = r_max - height[r]
                if diff > 0:
                    count += diff
                r_max = max(r_max, height[r])
        return count

