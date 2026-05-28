class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_dict = {")":"(", "}":"{", "]":"["}

        for ch in s:
            if ch in close_dict:
                if stack and stack[-1] == close_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if not stack:
            return True
        else:
            return False
        