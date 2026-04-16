class Solution:
    ## using extra space O(n)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        if n == 0:
            return 0
        
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        right_max[n-1] = height[n - 1]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j])

        for k in range(n):
            diff = min(left_max[k], right_max[k]) - height[k]
            res += diff
        return res
