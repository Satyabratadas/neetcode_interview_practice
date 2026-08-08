class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        countOpenClose = {")":"(", "}":"{", "]":"["}

        for ch in s:
            if ch in countOpenClose:
                if stack and stack[-1] == countOpenClose[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
                
        return True if not stack else False
        