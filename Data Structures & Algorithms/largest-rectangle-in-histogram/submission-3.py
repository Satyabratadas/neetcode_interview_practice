class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        s = []

        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                index, height = s.pop()
                start = index
                maxArea = max(maxArea, height * (i  - index))
            s.append((start, h))
        for i in range(len(s)):
            rec_height = s[i][1]
            rec_width = len(heights) - s[i][0]
            maxArea = max(maxArea, rec_height * rec_width)
        
        return maxArea