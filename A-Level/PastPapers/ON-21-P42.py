def Unknown(x,y):
  if x<y:
    print(x+y)
    return(Unknown(x+1,y)*2)
  elif x==y:
    return 1
  else:
    print(x+y)
    return(Unknown(x-1,y)//2)

print("10,15")
print("return value:",Unknown(10,15))

print("10,10")
print("return value:",Unknown(10,10))

print("15,10")
print("return value:", Unknown(15,10))


def IterativeUnknown(x,y):
  total=1
  while x!=y:
    if x<y:
      print(x+y)
      total=total*2
      x+=1
    else:
      print(x+y)
      total=total//2
      x-=1
  return total

print("10,15")
print("return value:",IterativeUnknown(10,15))

print("10,10")
print("return value:",IterativeUnknown(10,10))

print("15,10")
print("return value:", IterativeUnknown(15,10))


ArrayNodes=[[None,None,None]for i in range(20)] #ARRAY OF ARRAYS
RootPointer=-1 #INTEGER
FreeNode=0 #INTEGER

def AddNode(Arr,RP,FN):
  NodeData = int(input("Enter the data: "))
  if FN<=19:
    Arr[FN][0]=-1
    Arr[FN][1]=NodeData
    Arr[FN][2]=-1
    if RP==-1:
      RP=0
    else:
      placed=False
      curr=RP
      while placed==False:
        if NodeData<Arr[curr][1]:
          if Arr[curr][0]==-1:
            Arr[curr][0]=FN
            placed=True
          else:
            curr=Arr[curr][0]
        else:
          if Arr[curr][2]==-1:
            Arr[curr][2]=FN
            placed=True
          else:
            curr=Arr[curr][2]
    FN+=1
  else:
    print("Tree is Full")
  return RP,FN

def PrintAll():
  global ArrayNodes,RootPointer,FreeNode
  for i in ArrayNodes:
    print (i[0],i[1],i[2])

for i in range(10):
  RootPointer,FreeNode= AddNode(ArrayNodes,RootPointer,FreeNode)
PrintAll()

def InOrderTraversal(curr):
  global ArrayNodes
  if curr != -1:
    InOrderTraversal(ArrayNodes[curr][0])
    print(ArrayNodes[curr][1])
    InOrderTraversal(ArrayNodes[curr][2])

InOrderTraversal(RootPointer)