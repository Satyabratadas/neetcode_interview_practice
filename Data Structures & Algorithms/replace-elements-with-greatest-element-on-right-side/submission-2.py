class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_element = -1
        # for i in range(len(arr) - 1, -1, -1):
        for i in range (len(arr) - 1, -1, -1):
            if right_element > arr[i]:
                new_ele = right_element
            else:
                new_ele = arr[i]
            arr[i] = right_element
            right_element = new_ele
        return arr
