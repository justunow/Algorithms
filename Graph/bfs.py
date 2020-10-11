import collections

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
print(bfs(graph, 0))
