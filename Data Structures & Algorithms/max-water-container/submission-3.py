class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            current_area = h * (r - l)
            area = max(current_area, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area