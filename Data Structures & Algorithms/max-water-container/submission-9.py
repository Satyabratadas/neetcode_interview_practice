class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            weidth = right - left
            if heights[left] < heights[right]:
                currHeight = heights[left]
                left += 1
            else:
                currHeight = heights[right]
                right -= 1
            currArea = currHeight * weidth
            result = max(result, currArea)
        return result