class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if heights[i] < heights[j]:
        #             h = heights[i]
        #         else:
        #             h = heights[j]
        #         print(h)
        #         new_area = h * (j - i)
        #         print(new_area)
        #         if new_area > area:
        #             area = new_area
        # return area

        area = 0
        l = 0
        r = len(heights) - 1
        
        while l < r:
            if heights[l] < heights[r]:
                h = heights[l]
            else:
                h = heights[r]
            current_area = h * (r - l)
            if current_area > area:
                area = current_area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area