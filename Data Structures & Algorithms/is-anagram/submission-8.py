class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for ch in s:
            s_count[ch] = 1 + s_count.get(ch, 0)
        for ch in t:
            t_count[ch] = 1 + t_count.get(ch, 0)
        if s_count == t_count:
            return True
        return False