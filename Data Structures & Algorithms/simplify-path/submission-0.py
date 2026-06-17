class Solution:
    def simplifyPath(self, path: str) -> str:
        ch = ""
        stack = []

        for s in path + "/":
            if s == "/":
                if ch == ".." :
                    if stack:
                        stack.pop()
                elif ch != "" and ch != ".":
                    stack.append(ch)
                ch = ""
            else:
                ch += s
        return "/" + "/".join(stack)



        