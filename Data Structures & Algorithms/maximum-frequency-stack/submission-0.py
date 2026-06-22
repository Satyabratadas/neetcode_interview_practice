class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] = self.count.get(val, 0) + 1
        

    def pop(self) -> int:
        max_ele = max(self.count.values())
        i = len(self.stack) - 1
        while self.count[self.stack[i]] != max_ele:
            i -= 1
        self.count[self.stack[i]] -= 1
        max_ele -= 1
        return self.stack.pop(i)

        
        # if self.count[self.stack[-1]] > 1:
        #     self.count[self.stack.pop()] -= 1
        #     return self.stack.pop()
        # print(self.stack)
        # print(self.count)
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()