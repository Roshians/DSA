class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        col = []
        dia = []
        antiDia = []

        def helper(i):
            if i == n:
                ans.append(["".join(row) for row in board])
                return

            for j in range(n):

                if j in col or (i - j) in dia or (i + j) in antiDia:
                    continue

                col.append(j)
                dia.append(i - j)
                antiDia.append(i + j)
                board[i][j] = "Q"

                helper(i + 1)

                board[i][j] = "."
                col.remove(j)
                dia.remove(i - j)
                antiDia.remove(i + j)

        helper(0)
        return ans
