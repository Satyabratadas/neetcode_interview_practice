class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        self.swap(s, 0, n)
        
    def swap(self, arr, i, n):
        if i >= n//2:
            return
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        self.swap(arr, i+1, n)
