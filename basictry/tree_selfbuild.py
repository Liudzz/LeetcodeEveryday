class Node(object):
    def __init__(self,data = None, lchild = None, rchild = None):
        """
        :param data: 节点数据
        :param lchild: 左子树
        :param rchild: 右子树
        节点初始化
        """
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    def __init__(self):
        """树的根节点初始化"""
        self.root = Node()

    def add(self,data):
        node = Node(data)
        if self.isEmpty():  # 根节点不存在则插入节点为根节点
            self.root = node
        else:  # 根节点存在的时候则查找其左右子树为空插入
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild == None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild == None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)
    def pre_order(self,start):
        node = start
        if node == None:
            return
        print(node.data)
        if node.lchild == None and node.rchild ==None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self,start):
        node = start
        if node==None:
            return
        self.in_order(node.lchild)
        print(node.data)
        self.in_order(node.rchild)

    def post_order(self,start):
        node = start
        if node == None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.data)

    def pre_order_loop(self):
        if self.isEmpty():
            return

        stack = []
        node = self.root  # 根节点开始
        while node or stack:  # 当根节点或者栈任意不为空
            while node:  # 当根节点不为空
                print(node.data),  # 打印根节点的值
                stack.append(node)  # 栈中添加根节点
                node = node.lchild  # 打印下一左子树
            if stack:
                node = stack.pop()  # 开始
                node = node.rchild

    def isEmpty(self):
        return True if self.root.data == None else False

if __name__=="__main__":
    arr=[]
    for i in range(20):
        arr.append(i+1)
    tree = BinaryTree()
    for i in arr:
        tree.add(i)
    tree.pre_order(tree.root)
    tree.pre_order_loop()
    # tree.in_order(tree.root)
    # tree.post_order(tree.root)