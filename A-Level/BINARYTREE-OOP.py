class Node():
  def __init__(self,value):
    self.data = value
    self.left = None
    self.right = None

def createNode(val):
  return Node(val)


def AddChildNode(root,child):
  child=createNode(child)

  while True:
    if child.data<root.data:
      if root.left:
        root=root.left
      else:
        root.left=child
        print("Added to left")
        break
    else:
      if root.right:
        root=root.right
      else:
        root.right=child
        print("Added to right")
        break

def DelChildNode(root,target,parent=None):
  if root is None:
        return False
  
  if root.data==target:
    #Case 1: Leaf Node
    if root.left is None and root.right is None:
      if parent ==None:
        return None
      if parent.left==root:
        parent.left=None
      else:
        parent.right=None
      return True

    #Case 2: One Node attached
    elif root.left is None or root.right is None:
      child = root.left if root.left else root.right
      if parent is None:
        return child
      if parent.left==root:
        parent.left=child
      else:
        parent.right=child
      return True

    #Case 3: Two Nodes attached

    sucessor_parent=root
    sucessor=root.right

    while sucessor.left:
      sucessor_parent=sucessor
      sucessor=sucessor.left
    root.data=sucessor.data
    if sucessor_parent==root:
      root.right=sucessor.right
    else:
      sucessor_parent.left=sucessor.right
    return True
  elif target<root.data:
    return DelChildNode(root.left,target,root)
  else:
    return DelChildNode(root.right,target,root)