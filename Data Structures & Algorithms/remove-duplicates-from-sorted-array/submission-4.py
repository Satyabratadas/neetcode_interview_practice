class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_num = set()
        index = 0

        for num in nums:
            if num not in set_num:
                set_num.add(num)
                nums[index] = num
                index += 1
        return index