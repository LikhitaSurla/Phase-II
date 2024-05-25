def BinarySearch(arr,key):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==key:
            return "Found"
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return "Not Found"

arr=[1,2,3,4,5]
print(BinarySearch(arr,1))
        
    