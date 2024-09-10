#Breadth First Search
#It answers two type of questions i.) Is there a path from A to B  ii) what is the shortest path from A to B
#It uses queue mechanism 
#Runnning Time -> O(no. of edges) or we can mention O(V+E) where V is No. of Vertices and E is no. edges 
from collections import deque


#Bfs function 
def graphSearch(graph):
	search_queue = deque()
	search_queue += graph["A"]
	allreadySearched =[]
	while len(search_queue)!=0: 
		name=search_queue.popleft()
		#print("Allready Searched :",allreadySearched)
		print(name) #Grabs the first Person of the Queue
		#if not allreadySearched: 
		if(name=='D'):
			print("Found the Value")
			break
		else: 
			search_queue += graph[name]
			print(search_queue)
				#allreadySearched.append(name)

def printGraoh():
	for node, neighbors in graph.items(): 
		print(node,":",neighbors)

#Graph Creation 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#Calling BFS Function 
graphSearch(graph)