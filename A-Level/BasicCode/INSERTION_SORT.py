arr = [100, 10, 20, 15, 30, 25, 5, 25, 40, 1]
boundary = len(arr)

for i in range(1, boundary):
    if arr[i - 1] > arr[i]:
        k = i
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
                k = k - 1

print("Your output:    ", arr)