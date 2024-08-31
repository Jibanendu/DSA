#Binary Search : Only works when list is in sorted order .
#Code Assumption : List is in sorted Order 

def binary_search(sortArr, item):
	low=0
	high=len(sortArr)-1

	while low <=high:
		mid = (low+high)//2
		if sortArr[mid]<item:
			low=mid+1
		elif sortArr[mid]>item:
			high=mid-1
		else:
			return mid+1


sortArr= [2,5,6,8,10,15,100]
print(binary_search(sortArr, 5))