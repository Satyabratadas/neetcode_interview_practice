class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        count_num = set(nums)
        for num in nums:
            if (num - 1) not in count_num:
                length = 1
                while (num + length) in count_num:
                    length += 1
                longest = max(longest, length)
        return longest

        

        

        