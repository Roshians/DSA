class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ans = False
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*n
        visited[source] = True
        q = deque([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
        return False
        