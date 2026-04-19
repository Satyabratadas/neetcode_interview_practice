class NumArray:

    def __init__(self, nums: List[int]):
        pre_sum = 0
        self.pre_sum_arr = []
        for num in nums:
            pre_sum += num
            self.pre_sum_arr.append(pre_sum)
        print(self.pre_sum_arr)
        
    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.pre_sum_arr[left - 1] if left > 0 else 0
        right_sum = self.pre_sum_arr[right]
        result = right_sum - left_sum
        return result
        

