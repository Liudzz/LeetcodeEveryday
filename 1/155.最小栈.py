class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []

    def push(self, x: int) -> None:
        if len(self.a)==0:
            self.a.append((x,x))
        else:
            if x<=self.a[-1][1]:
                self.a.append((x,x))
            else:
                self.a.append((x,self.a[-1][1]))
        # self.a.append(x)


    def pop(self) -> None:
        self.a.pop()


    def top(self) -> int:
        return self.a[-1][0]


    def getMin(self) -> int:
        return self.a[-1][1]

if __name__=="__main__":
    obj = MinStack()
    obj.push(-2)
    print(obj.top())
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())




