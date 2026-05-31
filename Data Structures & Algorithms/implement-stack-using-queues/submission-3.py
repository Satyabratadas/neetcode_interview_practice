class MyStack:

    def __init__(self):
        self.s1 = deque()
        
    def push(self, x: int) -> None:
        self.s1.append(x)
        for i in range(len(self.s1) - 1):
            self.s1.append(self.s1.popleft())

    def pop(self) -> int:
        return self.s1.popleft()
        
    def top(self) -> int:
        return self.s1[0]
        
    def empty(self) -> bool:
        return len(self.s1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()