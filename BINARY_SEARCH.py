sorted_arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
search_value = int(input("Enter a value to search with: "))

FirstIndex = 0
LastIndex = len(sorted_arr) - 1
Found = False

while Found == False and FirstIndex <= LastIndex:
    
    MidIndex = (FirstIndex + LastIndex) // 2
    
    if search_value == sorted_arr[MidIndex]:
        Found = True
    elif search_value > sorted_arr[MidIndex]:
        FirstIndex = MidIndex + 1 
    else:
        LastIndex = MidIndex - 1   

if Found == False:
    print("Not in array")
else:
    # MidIndex holds the actual position of the element
    print(f"The position of the search value is {MidIndex}")