#Recursive Function 


def recursive_number(n):
	print(n)
	if n==0:   #Base Case - Used to end infinite loop and function doesn't call itself again 
		return
	else : 
		recursive_number(n-1) #Recursive Case - When the function calls itself again. 
		
recursive_number(5)