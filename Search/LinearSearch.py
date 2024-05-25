def LinearSearch(arr,key):
    
    for i in range(len(arr)):
        if arr[i]==key:
            return "Found"
    return "NotFound"
    
arr=[34,56,76,23,61,78,27]
print(LinearSearch(arr,76))