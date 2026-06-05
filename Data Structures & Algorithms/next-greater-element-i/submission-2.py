class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index = {}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums1)):
            nums1_index[nums1[i]] = i
            
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx =  nums1_index[val]
                res[idx] = curr
            if curr in nums1_index:
                stack.append(curr)
        return res


