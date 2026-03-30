class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = {}
        check_t = {}
        for ch in s:
            check_s[ch] = check_s.get(ch, 0) + 1
        for ch in t:
            check_t[ch] = check_t.get(ch, 0) + 1
        if check_s == check_t:
            return True
        else:
            return False