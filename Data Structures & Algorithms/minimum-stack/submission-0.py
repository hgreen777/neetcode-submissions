class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(
            min(val, self.minstack[-1]) 
            if len(self.minstack) >=1
            else val
        )
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        # Check for empty
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
