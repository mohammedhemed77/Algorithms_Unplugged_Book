# This is khan's algorithm in ch 5 of algorithms unplugged 
# note that sudo-code in this chapter has a typo 

# This code is claer , simple 
# Source : Geeks Of Geeks 
# https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/


from collections import deque
# We mainly take input graph as a set of edges. This function is
# mainly a utility function to convert the edges to an adjacency
# list
def constructadj(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj

# Function to return list containing vertices in Topological order
def topologicalSort(V, edges):
    adj = constructadj(V, edges)
    indegree = [0] * V

    # Calculate indegree of each vertex
    for u in range(V):
        for v in adj[u]:
            indegree[v] += 1

    # Queue to store vertices with indegree 0
    q = deque([i for i in range(V) if indegree[i] == 0])
    
    result = []
    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []

    return result

if __name__ == "__main__":
    V = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    result = topologicalSort(V, edges)
    if result:
        print("Topological Order:", result)