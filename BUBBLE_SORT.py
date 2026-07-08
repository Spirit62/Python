arr = [64, 34, 25, 12, 22, 11, 90]

boundary = len(arr) - 1
Swap = True

while Swap == True:
    Swap = False
    for i in range(0, boundary):
        if arr[i + 1] < arr[i]:
            
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            Swap = True
            
    boundary -= 1

print("Sorted array:", arr)
