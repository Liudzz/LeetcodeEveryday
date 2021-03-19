class Node:
    """链表节点，存放数据以及指向下一个节点地址"""
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinekedList:
    """链表初始化：创建头节点并依次插入数据与下一个节点"""
    def __init__(self):
        self.headval = None

    """打印链表"""
    def listprint(self):
        headnode = self.headval
        while headnode is not None:
            print(headnode.dataval)
            headnode = headnode.nextval
        print("^"*20)

    """头插法"""
    def headinsert(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    """尾插法"""
    def tailinsert(self,newdata):
        NewNode = Node(newdata)
        head = self.headval
        while(head.nextval != None):
            head = head.nextval
        head.nextval = NewNode

    """查找某一值,返回序列号"""
    def LookStar(self,data):
        head = self.headval
        i = 1
        while(head != None):
           if head.dataval == data:
               return i
           else:
               head = head.nextval
               i +=1
        return -1

    def MidInsert(self,i,data):
        if i==0:
            self.headinsert(data)
        newnode = Node(data)
        head = self.headval
        num = 1
        while head is not None:
            if num == i:
                newnode.nextval = head.nextval
                head.nextval = newnode
                return
            else:
                head = head.nextval
                num += 1
    # def ReverseList(head):
    #     mid = head
    #     pre = None
    #     next = mid.nextval
    #     while(mid != None):
    #         mid.nextval = pre
    #         pre = mid
    #         mid = next
    #         next = mid.nextval
    #     return pre

if __name__ == "__main__":
    list = LinekedList()
    list.headval = Node(1)
    d2 = Node(2)
    d3 = Node(3)

    list.headval.nextval = d2
    d2.nextval = d3

    list.listprint()

    list.MidInsert(3,5)
    # list.headinsert(0)
    #
    list.listprint()
    # p = Rever
    # list.ReverseList()
    list.listprint()
    #
    # list.tailinsert(5)
    #
    # list.listprint()

    # print(list.LookStar(3))