class Solution:
    ## Using two pointer space O(1)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        l, r, res = 0, n - 1, 0
        l_max, r_max = height[l], height[r]

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res

