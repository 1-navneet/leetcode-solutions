class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        grid_copy = deepcopy(grid)
        q = deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid_copy[r][c] == 2:
                    q.append((r,c))
                elif grid_copy[r][c] == 1:
                    fresh += 1
        minute = 0
        while len(q) != 0 and fresh > 0:
            minute += 1 
            rotten = len(q)
            for _ in range(rotten):
                i,j = q.popleft()
                for x,y in ([1,0],[0,1],[0,-1],[-1,0]):
                    new_i,new_j = i+x,j+y

                    if new_i < 0 or new_i == row or new_j < 0 or new_j == col:
                        continue
                    
                    if grid_copy[new_i][new_j] == 2 or grid_copy[new_i][new_j] == 0:
                        continue

                    grid_copy[new_i][new_j] = 2
                    fresh -= 1
                    q.append((new_i,new_j))
        if fresh > 0:
            return -1
        return minute

