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
def DeleteNode(root,target,parent=None):

  if root is None:
    return False


  if root[0]==target:


    #Case 1: Leaf Nodes
    if root[1]==None and root[2]==None:
      if parent==None:
        return None
      if parent[1]==root:
        parent[1]=None
      else:
        parent[2]=None
      return True

    #Case 2: One Child

    if root[1]==None or root[2]==None:
      child = root[1] if root[1] else root[2]
      if parent == None:
        return child
      if parent[1]==root:
        parent[1]=child
      else:
        parent[2]=child
      return True


    #Case 3: Two children

    sucessor_parent=root
    sucessor=root[2]

    while sucessor[1]:
      sucessor_parent=sucessor
      sucessor=sucessor[1]
    root[0]=sucessor[0]

    if sucessor_parent==root:
      root[2]=sucessor[2]
    else:
      sucessor_parent[1]=sucessor[2]
    return True

  
  elif root[0]> target:
    return DeleteNode(root[1],target,root)
  else:
    return DeleteNode(root[2],target,root)



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


