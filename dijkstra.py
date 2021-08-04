# Graph exemples
"""
    {
        'A': {'B': 6, 'D': 1},
        'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
        'C': {'B': 5, 'E': 5},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'C': 5, 'D': 1}
}

    {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

"""


import heapq


def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    priority_queue = [(0, starting_vertex)]
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


example_graph = {
        'A': {'B': 6, 'D': 1},
        'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
        'C': {'B': 5, 'E': 5},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'C': 5, 'D': 1}
}
print(dijkstra(example_graph, 'A'))
