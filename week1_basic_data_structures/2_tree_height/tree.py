class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getValue(self):
        return self.val

    def getNext(self):
        return self.next

    def __str__(self):
        return "Data: {} next : {}".format(self.val, self.next)


class Queue:
    def __init__(self):
        self.q = LinkedList()
        self.head = self.q.getNext()
        self.tail = self.q.getNext()
        self.size = 0

    def Enqueue(self, value):
        if not self.head:
            self.head = LinkedList(value)
            self.tail = self.head
        else:
            self.tail.next = LinkedList(value)
            self.tail = self.tail.next
        self.size += 1

    def DeQueue(self):
        if not self.head:
            return 'Queue is Empty'
        value = self.head.getValue()
        self.head = self.head.next
        self.size -= 1
        return value

    def Empty(self):
        return not self.head

    def getSize(self):
        return self.size

    def __str__(self):
        return "{}".format(self.head)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def getVal(self):
        return self.val

    def getChildren(self):
        return self.children

    def __str__(self):
        return "node {} has children: {}".format(self.val, [child.val for child in self.children])


def bfs(r, node, size):
    q = Queue()
    q.Enqueue(r)
    visited = [False] * size
    visited[r.getVal()] = True
    height = [0] * size
    m = 0
    while not q.Empty():
        start = q.DeQueue()
        # print(start.getVal(), end=' ')
        for child in start.getChildren():
            if not visited[child.getVal()]:
                q.Enqueue(child)
                height[child.getVal()] = height[start.getVal()] + 1
                visited[child.getVal()] = True
                m = max(m, height[child.getVal()])
    return m + 1


def bfs_eff(r):
    q = Queue()
    q.Enqueue(r)
    height = 0
    while not q.Empty():
        size = q.getSize()
        if size > 0:
            height += 1
        for i in range(size):
            start = q.DeQueue()
            for child in start.getChildren():
                q.Enqueue(child)
    return height


n = int(input())
parents = [int(x) for x in input().split()]
nodes = [TreeNode(i) for i in range(n)]
for child_index in range(n):
    if parents[child_index] == -1:
        root = nodes[child_index]
    else:
        nodes[parents[child_index]].add_child(nodes[child_index])

# for i in nodes:
#     print(i)
# print(bfs(root, nodes, n))
print(bfs_eff(root))

