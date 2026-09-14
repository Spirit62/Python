def createTreeNode(value):
  return [value,None,None]

def AddNode(root, node):
  node=createTreeNode(node)
  while True:
    if node[0]<root[0]:
      if root[1]:
        root=root[1]
      else:
        root[1]=node
        print("Added node to left of", root)
        break
    elif node[0]>root[0]:
      if root[2]:
        root=root[2]
      else:
        root[2]=node
        print("Added node to right of", root)
        break
    else:
      print("Value already exists in the tree")

def InOrderTraversal(root):
  if root is None:
    return
  InOrderTraversal(root[1])
  print(root[0])
  InOrderTraversal(root[2])

def PreOrderTraversal(root):
  if root is None:
    return
  print(root[0])
  PreOrderTraversal(root[1])
  PreOrderTraversal(root[2])

def PostOrderTraversal(root):
  if root is None:
    return
  PostOrderTraversal(root[1])
  PostOrderTraversal(root[2])
  print(root[0])