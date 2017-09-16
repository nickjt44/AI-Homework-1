import os

#Queue data structure for BFS
class Queue:

    def __init__(self):
        self.vals = []

    def add(self,val):
        #self.vals.insert(0,val)
        self.vals.append(val)

    def pop(self):
        return self.vals.pop(0)

    def empty(self):
        if len(self.vals) == 0:
            return True
        else:
            return False

#Stack data structure for DFS
class Stack:

    def __init__(self):
        self.vals = []

    def add(self,val):
        self.vals.insert(0,val)

    def pop(self):
        return self.vals.pop(0)

    def empty(self):
        if len(self.vals) == 0:
            return True
        else:
            return False

#Set data structure for expanded nodes
class Set:

    def __init__(self):
        self.vals = dict()

    def add(self,val):
        if val in self.vals:
            return
        else:
            self.vals[val] = 1

    def contains(self,val):
        if val in self.vals.keys():
            return True
        else:
            return False

#Priority Queue data structure for A*
class PriorityQueue:

    def __init__(self):
        self.vals = []

    def add(self,val,priority):
        self.vals.append((val,priority))
        self.vals = sorted(self.vals,key=lambda vals: vals[1])

    def pop(self):
        return self.vals.pop(0)

    def empty(self):
        if len(self.vals) == 0:
            return True
        else:
            return False
            
#Initializes the graph of the cities as a dictionary data structure
def initGraph():
    cities = dict()
    cities["oradea"] = [("zerind",71),("sibiu",151)]
    cities["zerind"] = [("oradea",71),("arad",175)]
    cities["arad"] = [("zerind",75),("timisoara",118),("sibiu",140)]
    cities["timisoara"] = [("arad",118),("lugoj",111)]
    cities["sibiu"] = [("arad",140),("rimnicu",80),("fagaras",99),("oradea",151)]
    cities["lugoj"] = [("timisoara",111),("mehadia",70)]
    cities["rimnicu"] = [("sibiu",80),("craiova",146),("pitesti",97)]
    cities["fagaras"] = [("sibiu",99),("bucharest",211)]
    cities["mehadia"] = [("lugoj",70),("drobeta",75)]
    cities["pitesti"] = [("rimnicu",97),("craiova",138),("bucharest",101)]
    cities["drobeta"] = [("mehadia",75),("craiova",120)]
    cities["craiova"] = [("drobeta",120),("rimnicu",146),("pitesti",138)]
    cities["bucharest"] = [("fagaras",211),("pitesti",101),("giurgiu",90),("urziceni",85)]
    cities["giurgiu"] = [("bucharest",90)]
    cities["urziceni"] = [("bucharest",85),("vaslui",142),("hirsova",98)]
    cities["vaslui"] = [("urziceni",142),("iasi",92)]
    cities["iasi"] = [("vaslui",92),("neamt",87)]
    cities["neamt"] = [("iasi",92)]
    cities["hirsova"] = [("urziceni",98),("eforie",86)]
    cities["eforie"] = [("hirsova",86)]
    return cities

#Breadth first search
class BFS:

    #Initializes data structures
    def __init__(self,start,dest):
        self.start = start
        self.dest = dest
        self.graph = initGraph()
        self.prev = dict() #logs the previous node to the node used as the key
        self.expanded = Set()

    #Calculates the resultant path from start to end
    def calcPath(self):
        node = self.dest
        vals = []
        while node != self.start:
            vals.insert(0,node)
            node = self.prev[node]
        vals.insert(0,self.start)
        return vals

    #Main search function
    def search(self): #start and dest are the city name strings
        q = Queue()
        q.add(self.start)

        while q.empty() == False:
            node = q.pop()
            if node == self.dest: #end node has been found
                print ("Success")
                print(self.expanded.vals.keys())
                endpath = self.calcPath()
                returnval = (endpath,len(self.expanded.vals.keys()))
                return returnval #Number of expanded nodes for problem 3(b)/(c)
            else:
                if not self.expanded.contains(node): #If the current node hasn't been expanded..
                    self.expanded.add(node) #expand it
                    for val in self.graph[node]: #children of expanded node
                        if val[0] not in q.vals and not self.expanded.contains(val[0]): #if a child isn't already in the queue and hasn't been expanded
                            self.prev[val[0]] = node #add the child to the queue
                            q.add(val[0])
        print ("Couldn't find destination")
        return

class DFS:

    #initializes data structures
    def __init__(self,start,dest):
        self.start = start
        self.dest = dest
        self.graph = initGraph()
        self.prev = dict()
        self.expanded = Set()

    #calculates the path from start to dest
    def calcPath(self):
        node = self.dest
        vals = []
        while node != self.start:
            vals.insert(0,node)
            node = self.prev[node]
        vals.insert(0,self.start)
        return vals
    
    def search(self): #start and dest are the city name strings
        st = Stack()
        g = initGraph()

        st.add(self.start)

        while st.empty() == False:
            node = st.pop()
            if node == self.dest:
                print ("Success")
                print(self.expanded.vals.keys())
                endpath = self.calcPath()
                returnval = (endpath,len(self.expanded.vals.keys()))
                return returnval
            else:
                if not self.expanded.contains(node):
                    self.expanded.add(node)
                    for val in self.graph[node]:
                        if val[0] not in st.vals and not self.expanded.contains(val[0]):
                            self.prev[val[0]] = node
                            st.add(val[0])
        print ("Couldn't find destination")
        return

class AStar:

    def __init__(self,start,dest):
        self.heuristic = dict()
        self.start = start
        self.dest = dest
        self.prev = dict()
        self.cost = dict()
        self.graph = initGraph()
        self.expanded = Set()

    #generates the heuristic from the (already calculated) distance data stored in cities/
    #the data is already calculated in order to be more efficient
    def generateHeuristic(self):
        for file in os.listdir("cities/"):
            path = "cities/" + file
            filename = file.split(".")[0]
            
            f = open(path,"r")
            self.heuristic[filename] = dict()
            mapping = dict()
            for line in f.readlines():
                lines = line.split(" ")
                self.heuristic[filename][lines[0]] = float(lines[1])

    #calculates the final path taken
    def calcPath(self):
        node = self.dest
        vals = []
        while node != self.start:
            vals.insert(0,node)
            node = self.prev[node]
        vals.insert(0,self.start)
        return vals

    #main search algorithm
    def search(self):
        self.generateHeuristic()
        q = PriorityQueue()

        q.add(self.start,self.heuristic[self.start][self.dest])
        self.cost[self.start] = 0

        while not q.empty():
            node = q.pop()
            if node[0] == self.dest:
                print("Success")
                print(self.expanded.vals.keys())
                endpath = self.calcPath()
                returnval = (endpath,len(self.expanded.vals.keys()))
                return returnval #expanded nodes for problem 3(b)/(c)
            else:
                self.expanded.add(node[0]) #expanded A* nodes
                for val in self.graph[node[0]]:
                    tempcost = self.cost[node[0]] + val[1]
                    k = self.cost.keys()
                    if val[0] not in k or (val[0] in k and tempcost < self.cost[val[0]]): #if a distance hasn't been given for a node or if
                        self.cost[val[0]] = tempcost                                      #the new distance to the node is shorter
                        q.add(val[0],tempcost + self.heuristic[val[0]][self.dest])        #then update the distance, and add the node to the priority
                        self.prev[val[0]] = node[0]                                       #queue with new priority, calculated from its current distance and heuristic distance
        print("Could not find dest")
        return

#loop over the algorithms for all cities for questions 3(b)/(c)
def searchloop():
    graph = initGraph()
    bfsnodes = dict()
    dfsnodes = dict()
    astarnodes = dict()
    nodes = dict()
    for city in graph.keys():
        for ct in graph.keys():
            bfs = BFS(city,ct)
            dfs = DFS(city,ct)
            astar = AStar(city,ct)
            x = dfs.search()[1]
            y = astar.search()[1]
            if x < y:
                nodes[(city,ct)] = (x,y)
    print(nodes)
            

        
        
#############CODE TO TEST THE PROGRAMS/ANSWER QUESTIONS#############      

##bfs1 = BFS("urziceni","mehadia")
##x = bfs1.search()
##dfs1 = DFS("urziceni","mehadia")
##y = dfs1.search()
##astar1 = AStar("urziceni","mehadia")
##a = astar1.search()
##print("bfs: ")
##print(x)
##print("dfs: ")
##print(y)
##print("astar: ")
##print(a)
#print("\nnext\n")
#DFS("sibiu","hirsova")
#x = AStar("mehadia","neamt")
searchloop()
