class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n = len(nums2)
        for num in nums1:
            greater_ele = -1
            for i in range(n-1, -1, -1):
                if nums2[i] > num:
                    greater_ele = nums2[i]
                elif nums2[i] == num:
                    break
            res.append(greater_ele)
        return res


