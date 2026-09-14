arr = [100, 10, 20, 15, 30, 25, 5, 25, 40, 1]
boundary = len(arr)

for i in range(1,boundary):
  if arr[i-1]>arr[i]:
    k=i
    for j in range(i-1,-1,-1):
      if arr[j]>arr[k]:
        arr[k],arr[j]=arr[j],arr[k]
        k=k-1

#Second method

arr = [100, 10, 20, 15, 30, 25, 5, 25, 40, 1]

for i in range(1,len(arr)):
    if arr[i-1]>arr[i]:
      key=arr[i]
      j=i-1
      while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
      arr[j+1]=key
    