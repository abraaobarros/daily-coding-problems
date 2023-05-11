import heapq

# Function to find the minimum spanning tree using Prim's algorithm
def prim_mst(graph):
    # Select an arbitrary start node
    start_node = list(graph.keys())[0]

    # Initialize the minimum spanning tree and set of visited nodes
    mst = []
    visited = set([start_node])
    edges = []
    for neighbor, weight in graph[start_node]:
        heapq.heappush(edges, (weight, start_node, neighbor))

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))

    return mst