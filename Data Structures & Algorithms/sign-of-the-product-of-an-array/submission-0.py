class Solution:
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        for num in nums:
            total *= num
        return self.signFunc(total)
    
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0