class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res_arr = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = 0
            for k in range(i, j):
                length = length * 10 + int(s[k])
            string = ""
            for i in range(j+1, j+1+length):
                string += s[i]
            print(string)
            res_arr.append(string)
            i = j + 1 + length
        return res_arr

