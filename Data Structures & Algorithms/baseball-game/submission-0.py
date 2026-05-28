class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == "+":
                stack.append(stack[-2] + stack[-1])
            
            elif op == "D":
                ele = stack[-1] * 2
                stack.append(ele)

            elif op == "C":
                stack.pop()
            
            else:
                stack.append(int(op))

        for num in stack:
            res += num

        return res
        