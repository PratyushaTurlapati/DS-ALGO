# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):
	# range(n) also work but outer loop will repeat one time more than needed.

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
a=[]
n=int(input("no.of elements:"))
for i in range(0,n):
    e=int(input())
    a.append(e)

bubbleSort(a)
x=[]
print ("Sorted array is:")
for i in range(len(a)):
	x.append(a[i])
print(x)
