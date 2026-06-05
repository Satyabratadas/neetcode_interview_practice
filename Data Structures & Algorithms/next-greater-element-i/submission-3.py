class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        result = [-1] * len(nums1)
        stack = []

        for i in range(len(nums1)):
            nums1_dict[nums1[i]] = i
        
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1_dict[val]
                result[idx] = curr
            if curr in nums1_dict:
                stack.append(curr)
        return result



