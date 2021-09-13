


class BT:
    def __init__(self, val, left=None, right=None) -> None:
       self.val = val
       self.left = left
       self.right = right
    
    def __str__(self) -> str:
        return str(self.val)


   
def inorder(node, func):
    if node.left:
        inorder(node.left, func)
    func(node)
    if node.right:
        inorder(node.right, func)


tree = BT(val=0, left=BT(1, left=BT(4)), right=BT(2))
inorder(tree, print)


# Morris Transversal Tree -> Optimise the memory of transversing tree
# Basically transverse inorder tree in O(1) in size
def inorder_morris(node:BT, func):
    curr = node
    while(curr):
        if not curr.left:
            func(curr.val)
            curr = curr.right
        else:
            rightMostDesc = curr.left
            while(rightMostDesc.right is not None and rightMostDesc.right.val != curr.val):
                rightMostDesc = rightMostDesc.right

            if rightMostDesc.right is None:
                rightMostDesc.right = curr
                curr = curr.left
            else:
                rightMostDesc.right = None
                func(curr)
                curr = curr.right
print('\n')
inorder_morris(tree, print)
