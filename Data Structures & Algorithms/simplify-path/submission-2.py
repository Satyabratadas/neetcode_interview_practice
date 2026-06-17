class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        file_names = path.split("/")
        for name in file_names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name != "" and name != ".":
                stack.append(name)
                
        return "/" + "/".join(stack)



        