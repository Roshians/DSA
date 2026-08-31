class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
        visited = [[False] * col for _ in range(row)]


        def bsf(r, c):
            visited[r][c] = True 
            q = deque([(r,c)])
            while q:
                cr, cc = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,-1), (0,1)):
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < row) and (0 <= nc < col) and grid[nr][nc] == "1" and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    count += 1
                    bsf(r,c)
        return count






        
