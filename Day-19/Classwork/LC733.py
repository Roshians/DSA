class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image
        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        visited = [[False] * n for _ in range(m)]
        visited[sr][sc] = True
        image[sr][sc] = color

        while q:
            r, c = q.popleft()
            for nr, nc in ((r + 1, c), (r, c - 1), (r - 1, c), (r, c + 1)):

                if (0 <= nr < m) and (0 <= nc < n) and not visited[nr][nc] and image[nr][nc] == start:
                    visited[nr][nc] = True
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image
