"""
Implementation of Breadth First Search
An alternative algorithm called Breath-First search provides us with the ability to return 
the same results as DFS but with the added guarantee to return the shortest-path first. 
This algorithm is a little more tricky to implement in a recursive manner instead using the queue data-structure, 
as such I will only being documenting the iterative approach. 
The actions performed per each explored vertex are the same as the depth-first implementation, 
however, replacing the stack with a queue will instead explore the breadth of a vertex depth before moving on. 
This behavior guarantees that the first path located is one of the shortest-paths present, based on number of edges being the cost factor.

We'll assume our Graph is in the form:
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

"""
Connected Component
Similar to the iterative DFS implementation the only alteration required is to remove the next item 
from the beginning of the list structure instead of the stacks last.
"""

def bfs(graph, start):
  visited, queue = set(), [start]
  while queue:
    vertex = queue.pop(0)
    print vertex
    if vertex not in visited:
      visited.add(vertex)
      print graph[vertex], visited, graph[vertex]-visited
      queue.extend(graph[vertex] - visited)
  return visited

print bfs(graph, 'A')

"""
Paths
This implementation can again be altered slightly to instead return all possible paths between two vertices,
the first of which being one of the shortest such path.
"""

def bfs_paths(graph, start, goal):
  queue = [(start, [start])]
  while queue:
    (vertex, path) = queue.pop(0)
    for next in graph[vertex] - set(path):
      if next == goal:
        yield path + [next]
      else:
        queue.append((next, path + [next]))

print list(bfs_paths(graph, 'A', 'F'))
#[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]


