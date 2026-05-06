# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1
        return self.sortArr(pairs, s, e)

    def sortArr(self, arr, s, e):
        if s >= e:
            return arr
        mid = (s + e) // 2
        self.sortArr(arr, s, mid)
        self.sortArr(arr, mid+1, e)
        self.merge(arr, s, mid, e)
        return arr
    def merge(self, arr, start, m, end):
        left = start
        right = m + 1
        c = []
        while left <= m and right <= end:
            if arr[left].key <= arr[right].key:
                c.append(arr[left])
                left += 1
            else:
                c.append(arr[right])
                right += 1
        while left <= m:
            c.append(arr[left])
            left += 1
        while right <= end:
            c.append(arr[right])
            right += 1
        for i in range(start, end+1):
            arr[i] = c[i - start]
        return arr


