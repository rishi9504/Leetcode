class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1=[x,*self.s1]
        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
