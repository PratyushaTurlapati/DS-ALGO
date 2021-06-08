a=[]
l=-1
n=int(input("noofelements:"))
for i in range(0,n):
    e=int(input())
    a.append(e)
s=int(input("search ele:"))
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
# Function call
result = binary_search(a, s)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

            
