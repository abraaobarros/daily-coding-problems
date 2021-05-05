
# Data structure

# Tree
class T():
    def __init__(self, val, children=None):
        self.val = val
        self.children = children

# Binary Search Tree


class BT():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right  = right

    # left is always lesser key node
    # right is always greater than key node
    def insert(self, val):
        if (val > self.val):
            if not self.right:
                self.right = BT(val)
            else:
                self.right.insert(val)
        elif val < self.val:
            if not self.left:
                self.left = BT(val)
            else:
                self.left.insert(val)

    # find the most left of right branch and switch to node
    def delete(self, val):
        if self.val == val:
            if not self.left:
                temp = self.right
                self = temp
                return
            if not self.right:
                temp = self.left
                self = temp
                return
            #find the lowest value bigger than value
            cur = self.right
            while(cur.left):
                cur = cur.left

            #just replace the node
            self.val = cur.val
            cur.val = val
            self.delete(val)
        else:
            if self.left:
                self.left.delete(val)
            if self.right:
                self.right.delete(val)
    
    def contains(self, val):
        if self.val == val:
            return self
        if self.left:
            left = self.left.contains(val)
        if self.right:
            right = self.right.contains(val)
        return right if right else left


def preorder(tree):
    queue = [(0,tree)]
    visited = {}
    while(len(queue)>0):
        h,cur = queue.pop(0)
        if h not in visited:
            visited[h]=[]
        visited[h].append(cur.val)
        if cur.left:
            queue.append((h+1, cur.left))
        if cur.right:
            queue.append((h+1, cur.right))
    return visited




b = BT(1)

b.insert(2)
b.insert(10)
b.insert(11)
b.insert(4)
print(preorder(b))
b.delete(1)
print(preorder(b))