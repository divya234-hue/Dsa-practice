from collections import deque
graph = {
    0:[1,2],
    1:[0,3],
    2:[0,4],
    3:[1],
    4:[2]
}
queue = deque()
visited = set()
queue.append(0)
visited.add(0)
while queue:
    Node = queue.popleft()
    print(Node)
    for neighbour  in  graph [Node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)