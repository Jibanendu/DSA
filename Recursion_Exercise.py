#Add up all the numbers in an Array using recursion 
#Count the elements in an Array using Recursion 
#Find the Maximum Number in a list 

def sum(arr):
	#BaseCase 
	if len(arr) ==0:
		return 0
	else:
		#RecursiveCase
		return arr[0]+sum(arr[1:])

def count(arr): 
	#Base Case 
	 if arr==[]:
	 	return 0; 
	 else: 
	 	#Recursive Case 
	 	return 1+ count(arr[1:])

def  maxNumber(arr):
	#Base Case 
	if len(arr)==0: 
		return 0
	elif len(arr)==1: 
		return arr[0]
	else : 
		#Recursive Case 
		max_of_rest = maxNumber(arr[1:])
		return arr[0] if arr[0] > max_of_rest else max_of_rest



arr=[1,2,3,4,5]
total =sum(arr)
count = count(arr)

print("SUM : ",total)
print("COUNT :",count)
print("Highest Number:",maxNumber(arr))

