from heapq import heappop, heappush

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar(graph, start, goal):
  
    open_set = []
    closed_set = set()

  
    parents = {}

  
    g_scores = {node: float('inf') for node in graph}
    f_scores = {node: float('inf') for node in graph}

    g_scores[start] = 0
    f_scores[start] = manhattan_distance(start, goal)
  
    heappush(open_set, (f_scores[start], start))

    while open_set:
        _, current = heappop(open_set)
        if current == goal:
          
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path

      
        closed_set.add(current)
        for neighbor in graph[current]:
            if neighbor in closed_set:
                continue
            tentative_g_score = g_scores[current] + 1
            if tentative_g_score < g_scores[neighbor]:
                parents[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = g_scores[neighbor] + manhattan_distance(neighbor, goal)
                if neighbor not in (node[1] for node in open_set):
                    heappush(open_set, (f_scores[neighbor], neighbor))

  
    return []

graph = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(graph, start, goal)

if path:
    print("Shortest path:")
    for node in path:
        print(node)
else:
    print("No path found.")