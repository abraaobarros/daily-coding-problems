class Node():
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def addChild(self, node):
        self.children.append(node)

# breadth first search iterativelly
def bfs(node:Node, func):
    queue = [node]
    while(len(queue)>0):
        cur = queue.pop(0)
        if cur not in visited:
            visited[cur]=True
            func(cur.val)
            for child in cur.children:
                queue.append(child)

visited={}
root = Node('1')
root.addChild(Node('2',[Node('16')]))
root.addChild(Node('3'))
root.addChild(Node('4'))
root.addChild(Node('5',[Node('13')]))
bfs(root, print)


class DisjointSet_QuickUnion():
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1] * size

    def find(self, a):
        if a == self.root[a]:
            return a
        self.root[a] = self.find(root[a])
        return self.root[a]

    def union(self, a,b):
        rootX = self.find[a]
        rootY = self.find[b]

        if rootX != rootY:
            # optimization to balancing the hight
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class DisjointSet_QuickFind():
    def __init__(self, size):
        self.root = [x for x in range(size)]

    def find(self, a):
        return self.root[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            for num in range(len(self.root)):
                if num == rootB:
                    self.root[num] = rootA