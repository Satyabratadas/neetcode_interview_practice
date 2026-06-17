class Solution:
    def decodeString(self, s: str) -> str:
        cur = ""
        k = 0
        stringStack = []
        countStack = []

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == "[":
                stringStack.append(cur)
                countStack.append(k)
                cur = ""
                k = 0
            elif ch == "]":
                temp = cur
                cur = stringStack.pop()
                count = countStack.pop()
                cur += temp * count
            else:
                cur += ch
        return cur

