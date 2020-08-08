class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def min_depth_bst(root):
  if(root is None):
    return 

  if(root.left is None or root.right is None):
    return 1
  else:
    return 1 + min(min_depth_bst(root.left), min_depth_bst(root.right))
  

n3 = Node(3, None, Node(4))
n2 = Node(2, Node(3))
n1 = Node(1, n2, n3)
root = Node(5, n1, None)

print(min_depth_bst(root))