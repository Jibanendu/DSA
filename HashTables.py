#Hash Tables

voted = {}

def check_voter(name):
	if voted.get(name): 
		print("Already Voted")
	else:
	   voted[name]=True
	   print("Not voted Yet")


check_voter("Jiban")