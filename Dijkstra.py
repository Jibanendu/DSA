#Dijkstra Algorithm only works with directed Acyclic Graph 
#This algorithm will not work if it has negative weight edges. For Negative weight edges we can used Bellman-Ford Algorithm 

#Finding the lowest value in the Costs Table 
def find_lowest_cost_node(costs):

	smallest_value = float("inf")
	smallest_node = None

	for node in costs: 
		#print(node,":",costs[node])
		if costs[node] < smallest_value and node not in processed:
			smallest_value=costs[node]
			smallest_node= node
	print(smallest_value,":",smallest_node)
	return smallest_node



#Graph Table is Created

#Graph Nodes are Created
graph={}
graph["start"]={}
graph["a"]={}
graph["b"]={}
graph["fin"]={}

#Graph Weights are added 
graph["start"]["a"]=6
graph["start"]["b"]=2
graph["a"]["fin"]=1
graph["b"]["fin"]=5
graph["b"]["a"]=3

#Costs table is created 

#Infinity value will provided to fin/ end target initially 
infinity = float("inf")

costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity


#Parents Table is created 
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None


#Processed Array -> to keep track of all the nodes we have processed already
processed=[]

node= find_lowest_cost_node(costs)
#print(costs[node])

while node is not None:
	cost = costs[node]
	neighbor_node =graph[node]
	for n in neighbor_node.keys():
		new_cost = cost+neighbor_node[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n]=node
	processed.append(node)

	node= find_lowest_cost_node(costs)
	

