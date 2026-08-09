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
  if root.data==target:
    #Case 1: Leaf Node
    if root.left is None and root.right is None:
      