class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = {}
        check_t = {}
        for ch in s:
            if ch not in check_s:
                check_s[ch] = 1
            else:
                check_s[ch] += 1
        for ch in t:
            if ch not in check_t:
                check_t[ch] = 1
            else:
                check_t[ch] += 1
        if check_s == check_t:
            return True
        else:
            return False