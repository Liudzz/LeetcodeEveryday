class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a=[]

    def push(self, x: int) -> None:
        if not len(self.a):
            self.a.append((x,x))
        else:
            if x<self.a[-1][1]:
                self.a.append((x,x))
            else:
                self.a.append((x,self.a[-1][1]))


    def pop(self) -> None:
        self.a.pop()


    def top(self) -> int:
        return self.a[-1][0]


    def getMin(self) -> int:
        return self.a[-1][1]

if __name__=="__main__":
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-3)
    print(a.getMin())
    a.pop()
    print(a.top())
    print(a.getMin())