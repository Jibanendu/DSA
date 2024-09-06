#QuickSort - Divide & Conquer - Recursion needs to be added 
# It is much faster than Selection Sort
#Quick Sort Time Complexity is O(n* log n)

def quickSort(arr):
	if len(arr) <2:
		return arr  #Base Case 
	else:           #Recursive Case
		pivot = arr[0]
		less=[]
		greater=[]

		for i in arr[1:]:
			if i<pivot:
				less.append(i)
			else:
				greater.append(i)
		return quickSort(less)+[pivot]+quickSort(greater)


arr=[10,5,2,3,40]
print(quickSort(arr))