class Solution:
    def simplifyPath(self, path: str) -> str:
        path_str = path.split('/')
        stack = []
        for path in path_str:
            if path == "..":
                if stack:
                    stack.pop()
            elif path != "" and path != ".":
                stack.append(path)

        return "/" + "/".join(stack)



        