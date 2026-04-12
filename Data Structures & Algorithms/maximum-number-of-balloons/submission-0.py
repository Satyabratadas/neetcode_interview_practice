class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = {}
        balloon = "balloon"
        b_text = {}
        for s in balloon:
            b_text[s] = 1 + b_text.get(s, 0)
        res = len(text)
        for ch in text:
            countText[ch] = 1 + countText.get(ch, 0)
        for c in b_text:
            res = min(res, countText.get(c, 0) // b_text.get(c, 0))
        return res