# Python program to print all paths from a source to destination.
  
from collections import defaultdict
  

def addEdge(u,v):
    graph[u].append(v)

def printAllPathsUtil(u, d, visited, path):

    visited[u]= 1
    path.append(u)

    if u == d:
        print path
    else:
        for i in graph[u]:
            if visited[i]==0:
                printAllPathsUtil(i, d, visited, path)
                 
    path.pop()
    visited[u]= 0


def printAllPaths(s, d):
    visited =[0 for _ in range(V)]

    printAllPathsUtil(s, d,visited, [])
  
  
  
# Create a graph given in the above diagram
V = 4 
graph = defaultdict(list) 

addEdge(0, 1)
addEdge(1, 0)
addEdge(2, 0)
addEdge(3, 0)
addEdge(0, 2)
addEdge(0, 3)
addEdge(2, 1)
addEdge(1, 3)
addEdge(1, 2)
addEdge(3, 1)
  
s = 2 ; d = 3
printAllPaths(s, d)