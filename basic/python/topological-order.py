
def dfs(graph, node, visited, stack):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)

    stack.append(node)

def topologicalSort(graph):
    visited = {node: False for node in graph}
    stack = []

    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, stack)

    return stack[::-1]

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

sorted_nodes = topologicalSort(graph)
print(sorted_nodes)