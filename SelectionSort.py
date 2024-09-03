#Selection Sort  : O(nXn)time
# Selection Sort is a neat algorithm but not very fast 

def findSmallestArr(arr):
	smallest = arr[0]
	smallest_index=0

	for i in range(1,len(arr)):
		if arr[i]< smallest: 
			smallest = arr[i]
			smallest_index=i
	return smallest_index


def selectionSort(arr): 
	newArr=[]
	for i in range(len(arr)):
		smallest = findSmallestArr(arr)
		newArr.append(arr[smallest])

		print("During Sorting",arr)
		print("New Sort",newArr)

		arr.pop(smallest)




arr =[5,3,6,2,10]
print("Before Sorting",arr)
selectionSort(arr)


