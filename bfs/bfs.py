# bfs implementation

graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": [],
    "e": ['b'],
    "f": ['d']
}


def breathFirstSearch(graph, node):
    # queue for search
    queue = [node]
    
    while len(queue) > 0 :
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

breathFirstSearch(graph, 'f')

