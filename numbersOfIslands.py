def dfs(islands, r, c):
    rn = len(islands)
    cn = len(islands)
    islands[r][c] = "0"
    if r-1>= 0 and islands[r][c] == "1":
        self.dfs(islands, r-1, c)

    if r+1 < rn and islands[r+1][c] == "1":
        self.dfs(islands, r+1, c)

    