## Using Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        return self.mergeSort(nums, start, end)

    def mergeSort(self, arr, start, end):
        if start >= end:
            return arr
        mid = (start + end) // 2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid+1, end)
        self.mergearr(arr, start, mid, end)
        return arr
        
    def mergearr(self, arr, s, m, e):
        c = []
        left = s
        right = m+1
        while left <= m and right <= e:
            if arr[left] < arr[right]:
                c.append(arr[left])
                left += 1
            else:
                c.append(arr[right])
                right += 1
        while left <= m:
            c.append(arr[left])
            left += 1
        while right <= e:
            c.append(arr[right])
            right += 1
        for i in range(s, e+1):
            arr[i] = c[i - s]
        return arr