class Solution:
    def decodeString(self, s: str) -> str:
        current = ""
        k = 0
        stringStack = []
        countStack = []

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == "[":
                stringStack.append(current)
                countStack.append(k)
                current = ""
                k = 0
            elif ch == "]":
                temp = current
                current = stringStack.pop()
                count = countStack.pop()
                current += temp * count
            else:
                current += ch
        return current


