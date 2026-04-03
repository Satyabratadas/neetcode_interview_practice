class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_arr = []
        total = 0
        for num in nums:
            total += num
            self.prefix_arr.append(total)
    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_arr[right]
        if left > 0:
            left_sum = self.prefix_arr[left - 1]
        else:
            left_sum = 0
        return right_sum - left_sum

