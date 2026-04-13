class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_set = {}
        final_map = []
        for i, num in enumerate(nums2):
            num2_set[num] = i
        for num in nums1:
            final_map.append(num2_set[num])
        return final_map

        