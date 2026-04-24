class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for ch in s:
            if ch.isalnum():
                clean_str += ch.lower()
        n = len(clean_str)
        return self.checkPalindrome(0, n, clean_str)
    
    def checkPalindrome(self, i, n, arr):
        if i >= n // 2:
            return True
        if arr[i] != arr[n-1-i]:
            return False
        return self.checkPalindrome(i+1, n, arr)
        
