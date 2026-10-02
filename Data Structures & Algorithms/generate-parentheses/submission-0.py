class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        self.backTrack(0, 0, res, n, [])
        return res
    
    def backTrack(self, openN, closeN, res, n, st):
        if openN == closeN == n:
            res.append("".join(st))
            return
        
        if openN < n:
            st.append('(')
            self.backTrack(openN + 1, closeN, res, n, st)
            st.pop()
        if closeN < openN:
            st.append(')')
            self.backTrack(openN, closeN + 1, res, n, st)
            st.pop()
        