class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0
        num_set = set(nums)

        for num in nums:
            if (num-1) not in num_set:
                l = 1
                while num + l in num_set:
                    l += 1
                long = max(long, l)
        return long
        

        

        