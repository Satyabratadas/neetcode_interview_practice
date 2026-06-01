class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s1 = []

        for ch in tokens:
            if ch == "+":
                s1.append(s1.pop() + s1.pop())
            elif ch == "-":
                a, b = s1.pop(), s1.pop()
                s1.append(b - a)
            elif ch == "*":
                s1.append(s1.pop() * s1.pop())
            elif ch == "/":
                a, b = s1.pop(), s1.pop()
                s1.append(int(b / a))
            else:
                s1.append(int(ch))
        return s1.pop()
    