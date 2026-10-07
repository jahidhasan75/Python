def dfs(start, adj, n):
    visited = [False] * (n + 1)
    stack = [start]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            # ascending order maintain everse 
            for neighbor in reversed(adj[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)


# ===== Graph from image =====
n = 5

adj = {
    1: [2, 3, 4],
    2: [3],
    3: [1, 4, 5],
    4: [2, 5],
    5: [4],
}

# adjacency list sort
for i in adj:
    adj[i].sort()

print("DFS Traversal:")
dfs(1, adj, n)
