class MinStack:

    def __init__(self):
        self.list=[] #[5,3,4,1]
        self.mindata=[] 
        
    def push(self, val: int) -> None:
        self.list.append(val)
        # self.mindata = min(self.mindata,val)
        if not self.mindata or val <= self.mindata[-1]: #[5,3]
            self.mindata.append(val)
        
    def pop(self) -> None:
        popped = self.list.pop()
        if popped == self.mindata[-1]:
            self.mindata.pop()
        

    def top(self) -> int:
        return self.list[-1]
        
    def getMin(self) -> int:
        return self.mindata[-1]



        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
