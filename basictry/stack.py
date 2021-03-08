# init,push,pop,peek,isEmpty,size

class Stack():
    def __init__(self):
        self.stack = []
    def push(self,num):
        self.stack.append(num)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        if len(self.stack):
            return False
        else:
            return True
    def size(self):
        return len(self.stack)
    def show(self):
        return self.stack

if __name__=="__main__":
    stack = Stack()
    print(stack.show())
    print(stack.isEmpty())
    stack.push("hello,stack")
    stack.push(1)
    print(stack.peek())
    print(stack.show())
    print(stack.size())
    stack.pop()
    print(stack.show())
