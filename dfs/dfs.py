# dfs implementation
graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": [],
    "e": ['b'],
    "f": ['d']
}

def depthFirstSearch(graph, node):
    # stack
    stack = [node]
    while len(stack)>0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

depthFirstSearch(graph, 'a')
