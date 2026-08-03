Stack = [None for _ in range(5)]
StartPointer = 0
Boundary = len(Stack)


def push(value):
  global StartPointer,Boundary
  if StartPointer<Boundary:
    Stack[StartPointer]=value
    StartPointer+=1
    print("Added")
  else:
    print("Stack is full")

def pop():
  global StartPointer, Boundary
  if StartPointer > 0:
      StartPointer -= 1
      item = Stack[StartPointer]
      Stack[StartPointer] = None  
      print("Removed")
      return item
  else:
      print("Stack is empty")
      return None
  
push(10)
push(20)
pop()
pop()
print(Stack)