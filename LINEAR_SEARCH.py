arr=[1,2,3,4,5,6,7,8]

def search(value):
  found=-1
  global arr
  for i in range(len(arr)):
    if arr[i]==value:
      found=i
      break
  if found !=-1:
    print("Value found")
  else:
    print("Value not found")
  return found

search(10)