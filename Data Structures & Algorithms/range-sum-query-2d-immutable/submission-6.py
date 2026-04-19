class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.pre_sum_mat = [[0] * (cols + 1) for i in range(rows + 1)]
        for r in range(rows):
            leftsum = 0
            for c in range(cols):
               leftsum += matrix[r][c]
               above = self.pre_sum_mat[r][c+1]
               self.pre_sum_mat[r+1][c+1] = above + leftsum 
        print(self.pre_sum_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        bottom_right = self.pre_sum_mat[r2][c2]
        left = self.pre_sum_mat[r2][c1 - 1]
        above = self.pre_sum_mat[r1 - 1][c2]
        top_left = self.pre_sum_mat[r1 - 1][c1 - 1]
        result = bottom_right - left - above + top_left
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)