class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == "+":
                val = stack[-2] + stack[-1]
                stack.append(val)
                res += val
            
            elif op == "D":
                val = stack[-1] * 2
                stack.append(val)
                res += val

            elif op == "C":
                val = stack[-1]
                stack.pop()
                res -= val
            
            else:
                val = int(op)
                stack.append(val)
                res += val

        return res
        