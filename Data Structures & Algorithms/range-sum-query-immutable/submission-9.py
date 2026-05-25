class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = []
        total = 0
        for num in nums:
            total += num
            self.presum.append(total)
        
    def sumRange(self, left: int, right: int) -> int:
        presum_right = self.presum[right]
        presum_left = 0
        if left > 0:
            presum_left = self.presum[left-1]
        return presum_right - presum_left
        
        

