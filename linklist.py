"""

    linklist.py
    功能：实现单链表的构建和操作

    以及各种类的构建

"""

from Tool.common.queue import LQueue


# 节点类
class Node:
    """
        思路：自定义的类设为节点类，类中的属性为数据内容
            next属性用来和下一个节点建立联系
    """

    def __init__(self, value, next=None):
        """
            构造函数
        :param value: 节点值
        :param next: 引用下一个节点
        """
        self.value = value
        self.next = next


# 树节点类
class TreeNode:
    def __init__(self, value, next_left=None, next_right=None):
        self.value = value
        self.next_left = next_left
        self.next_right = next_right


# 二叉树类
class Bitree:
    def __init__(self, root):
        self.root = root

    # 先序遍历
    def preOreder(self, node):
        if node is None:
            return
        print(node.value)
        self.preOreder(node.next_left)
        self.preOreder(node.next_right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.next_left)
        print(node.value)
        self.inOrder(node.next_right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.next_left)
        self.postOrder(node.next_right)
        print(node.value)

    # 层次遍历
    def levelOrder(self, node):
        """
            node先入队，循环判断，队列不为空时，出队表示遍历
            同时让出队元素的左右孩子入队
        """
        if node is None:
            return
        lq = LQueue()
        lq.enqueue(node)
        while not lq.is_empty():
            node = lq.dequeue()
            print(node.value)
            if node.next_left:
                lq.enqueue(node.next_left)
            if node.next_right:
                lq.enqueue(node.next_right)


# 链式线性列表操作类
class LinkList:
    """
        思路：生成单链表，通过实例化的对象就代表一个链表
             可以调用具体的操作方法完成各种功能
    """

    def __init__(self):
        # 链表的初始化节点，没有有用数据，但是便于标记链表的开端
        self.head = Node(None)


    # 初始化链表
    def init_list(self, list_link):
        """
            初始化链表，添加一组节点
        :param list_link: 包含链表基础值的可迭代对象
        """
        # p 作为移动变量
        self.data = [x for x in list_link]
        p = self.head
        for i in list_link:
            # 遍历到一个值就创建一个节点
            p.next = Node(i)
            p = p.next

    def __len__(self):
        """
            此方法是len()函数调用，此方法返回的必须是整数
        :return: len的结果
        """
        count = 0
        p = self.head
        while p.next:
            count += 1
            p = p.next
        return count


    # 遍历链表
    def show(self):
        p = self.head.next  # p代表第一个有值的节点
        while p:
            print(p.value)
            p = p.next  # p向后移动

    # 判断链表是否为空
    def is_empty(self):
        """
            判断链表是否为空
        :return: 空返回True 否则返回False
        """
        if self.head.next is None:
            return True
        return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def insert_last(self, value):
        """
            在最后追加指定节点
        :param value: 指定节点的值
        """
        p = self.head
        # p移动到最后一个节点
        while p.next:
            p = p.next
        p.next = Node(value)  # 最后添加节点

    # 头部插入
    def insert_head(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入（通过值）
    def insert_previous(self, index_value, value):
        """
            在第一个指定节点前插入节点
        :param index_value: 指定节点的值
        :param value: 插入节点的值
        """
        p = self.head
        while p.next.value != index_value:
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    def insert_next(self, index_value, value):
        """
            在第一个指定节点后插入节点
        :param index_value: 指定节点的值
        :param value: 插入节点的值
        :return:
        """
        p = self.head.next
        while p.value != index_value:
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    # 指定位置插入（通过索引）
    def insert_index_previous(self, index, value):
        """
            在指定索引前插入节点
        :param index: 指定的索引
        :param value: 插入节点的值
        """
        if index < 0:
            raise IndexError("index out of range")
        p = self.head
        for i in range(index):
            if not p.next:
                break
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    def insert_index_next(self, index, value):
        """
            在指定索引后插入节点
        :param index: 指定的索引
        :param value: 插入节点的值
        """
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            if not p.next:
                break
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    # 删除节点（通过值）
    def remover_by_value(self, value):
        """
            删除值为指定值的第一个节点
        :param value: 指定值
        """
        p = self.head
        while p.next.value != value and p.next:
            p = p.next
        if not p.next:
            raise ValueError(value, "not in linklist")
        p.next = p.next.next

    # 删除节点（通过索引）
    def remover_by_index(self, index):
        """
            删除指定索引的节点
        :param index: 指定的索引
        """
        if index < 0:
            raise IndexError("index out of range")
        p = self.head
        for i in range(index):
            if not p.next:
                break
            p = p.next
        p.next = p.next.next  # 超出则为None

    # 获取某个节点的索引（通过值）
    def search_by_value(self, value):
        """
            获取值为指定值的第一个节点的索引
        :param value: 指定的值
        :return 值为指定值的第一个节点的索引
        """
        p = self.head
        index = 0
        while p.next.value != value and p.next:
            p = p.next
            index += 1
        if not p.next:
            raise ValueError(value, "is not find")
        return index

    # 获取某个节点的值（通过索引）
    def search_by_index(self, index):
        """
            获取指定索引的节点的值
        :param index: 指定索引
        :return 指定索引节点的值
        """
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            if not p:
                raise IndexError("index out of range")
            p = p.next
        return p.value


if __name__ == "__main__":
    # 初始化一组数据
    l = [1, 2, 4, 3, 4]

    # 想有一个链表
    link = LinkList()
    link.init_list(l)
    # link.insert_previous(4,5)
    # link.clear()
    # link.show()
    # link.search_by_value(4)
    link.insert_last(5)
    link.show()
