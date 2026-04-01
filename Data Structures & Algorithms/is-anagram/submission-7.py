from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = Counter(s)
        check_t = Counter(t)
        return check_s == check_t