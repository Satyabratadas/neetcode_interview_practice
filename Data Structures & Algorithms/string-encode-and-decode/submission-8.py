class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = []
        for s in strs:
            encodedStr.append(str(len(s)))
            encodedStr.append("$")
            encodedStr.append(s)
        return "".join(encodedStr)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result
        

