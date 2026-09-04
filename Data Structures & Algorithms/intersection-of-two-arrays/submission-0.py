class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        result = set()

        for num in nums1:
            l = 0 
            r = len(nums2) - 1
            while l <= r:
                mid = l + (r - l) // 2
                
                if nums2[mid] == num:
                    result.add(num)
                    break
                elif nums2[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
        return list(result)