# code Source : https://www.geeksforgeeks.org/dsa/detect-cycle-in-a-graph/
# [Approach 2] Using Topological Sorting - O(V + E) Time and O(V) Space


# Helper function for DFS-based cycle detection
def isCyclicUtil(adj, u, visited, recStack):
    # If the node is already in the current recursion stack, a cycle is detected
    if recStack[u]:
        return True

    # If the node is already visited and not part of the recursion stack, skip it
    if visited[u]:
        return False

    # Mark the current node as visited and add it to the recursion stack
    visited[u] = True
    recStack[u] = True

    # Recur for all the adjacent vertices
    for v in adj[u]:
        if isCyclicUtil(adj, v, visited, recStack):
            return True

    # Remove the node from the recursion stack before returning
    recStack[u] = False
    return False

# Function to build adjacency list from edge list


def constructadj(V, edges):
    adj = [[] for _ in range(V)]  # Create a list for each vertex
    for u, v in edges:
        adj[u].append(v)  # Add directed edge from u to v
    return adj

# Main function to detect cycle in the directed graph


def isCyclic(V, edges):
    adj = constructadj(V, edges)
    visited = [False] * V       # To track visited vertices
    recStack = [False] * V      # To track vertices in the current DFS path

    # Try DFS from each vertex
    for i in range(V):
        if not visited[i] and isCyclicUtil(adj, i, visited, recStack):
            return True  # Cycle found
    return False  # No cycle found


# Example usage
V = 4  # Number of vertices
edges = [[0, 1], [1, 2], [2, 0], [2, 3]]

print(isCyclic(V, edges))