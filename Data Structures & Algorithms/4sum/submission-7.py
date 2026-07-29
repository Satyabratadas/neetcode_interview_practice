class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            for j in range(i+1, len(nums)):
                b = nums[j]
                if j > i + 1 and b == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    total = a + b + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([a, b, nums[left], nums[right]])
                        left, right = left + 1, right - 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
        return result



        