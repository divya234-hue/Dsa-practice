graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}
visited = set()
def dfs(Node):
    visited.add(Node)
    print(Node)
    for neighbour in graph[Node]:
        if neighbour not in visited:
            dfs(neighbour)
dfs(0)