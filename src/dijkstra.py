from src.heap_priority_queue import HeapPriorityQueue


def dijkstra(graph, start, target = None):
    distances = {}
    for node in graph.nodes:
        distances[node] = float("inf")

    previous = {}
    for node in graph.nodes:
        previous[node] = None

    distances[start] = 0

    queue = HeapPriorityQueue()
    queue.add(0, start)

    while not queue.is_empty():
        current_distance, current_node = queue.remove_min()

        if current_distance > distances[current_node]:
            continue

        if current_node == target and target is not None:
            break
        
        neighbours = graph.neighbours(current_node)
        for neighbour, weight in neighbours.items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current_node
                queue.add(new_distance, neighbour)
    
    return distances, previous