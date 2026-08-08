def createTreeNode(value):
  return [value, None,None]

def AddChildNode(root,value):
  value=createTreeNode(value)
  while True:
    if value[0]< root[0]:
      if root[1]:
        root=root[1]
      else:
        root[1]=value
        print("Added to left")
        break
    else:
      if root[2]:
        root=root[2]
      else:
        root[2]=value
        print("Added to right")
        break

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
root = createTreeNode(10)

# Add elements
AddChildNode(root, 5)
AddChildNode(root, 15)
AddChildNode(root, 3)
AddChildNode(root, 7)

# Print sorted output
print("\nIn-Order Traversal:")
InOrderTraversal(root)

print("\nPre-Order Traversal:")
PreOrderTraversal(root)

print("\nPost-Order Traversal:")
PostOrderTraversal(root)


