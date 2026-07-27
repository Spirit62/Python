
arr=[64, 34, 25, 12, 22, 11, 90]
boundary=len(arr)-1
swap = True
while swap==True and boundary>0:
    swap=False
    for i in range(boundary):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swap = True
    boundary-=1

print("Sorted array:", arr)