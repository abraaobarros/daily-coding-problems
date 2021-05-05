class Node():
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
    
    def addChild(self, node):
        self.children.append(node)

# iterativelly
def bfs(node:Node, func):
    queue = [node]
    while(len(queue)>0):
        cur = queue.pop()
        func(cur.val)
        for child in cur.children:
            queue.append(child)


