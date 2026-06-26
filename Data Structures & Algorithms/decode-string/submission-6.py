class Solution:
    def decodeString(self, s: str) -> str:
        strStack = []
        cStack = []
        n = 0
        curr = ""
        for ch in s:
            if ch.isdigit():
                n = n * 10 + int(ch)
            elif ch == "[":
                strStack.append(curr)
                cStack.append(n)
                curr = ""
                n = 0
            elif ch == "]":
                temp = curr
                curr = strStack.pop()
                count = cStack.pop()
                curr += temp * count
            else:
                curr += ch
        return curr


