class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        balloon_count = Counter('balloon')
        res = len(text)

        print(text_count)
        print(balloon_count)
        
        for ch in balloon_count:
            res = min(res, text_count[ch] // balloon_count[ch])
        return res
