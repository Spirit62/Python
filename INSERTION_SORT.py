arr=[42, -5, 0, 3.14, 42, -5, 100]
boundary= len(arr)
for i in range(1,boundary):
  k=i
  for j in range(i-1,-1,-1):
    if arr[k] < arr[j]:
            arr[k], arr[j] = arr[j], arr[k]
            k = k - 1
    else:
      break

print(arr)