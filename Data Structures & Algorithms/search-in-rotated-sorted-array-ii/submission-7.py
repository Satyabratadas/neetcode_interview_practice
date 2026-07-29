class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            ## Search in left sorted portion
            elif nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            ## search in right sorted portion
            else:
                if target < nums[mid] or target > nums[right] :
                    right = mid - 1
                else:
                    left = mid + 1
        return False
