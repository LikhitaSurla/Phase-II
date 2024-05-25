def BubbleSort(arr):
    n=len(arr)
    fixThisPosition=n-1
    
    while(fixThisPosition>0):
        for index in range(0,fixThisPosition):
            if arr[index]>arr[index+1]:
                arr[index],arr[index+1]=arr[index+1],arr[index]
        print(arr)
        fixThisPosition-=1
arr=[56,23,67,89,21,19,7,95]
# print(arr)
BubbleSort(arr)
print(arr)