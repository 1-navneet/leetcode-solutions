class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        row = len(image)
        col = len(image[0])
        seen = image[sr][sc]
        q = deque()
        image_copy = deepcopy(image)

        image_copy[sr][sc] = color
        q.append((sr,sc))
        while len(q) != 0:
            i,j = q.popleft()
            for x,y in ([1,0],[0,1],[-1,0],[0,-1]):
                new_i,new_j = i+x,j+y

                if new_i < 0 or new_i == row or new_j < 0 or new_j == col:
                    continue
                if image_copy[new_i][new_j] == color:
                    continue
                
                if image_copy[new_i][new_j] == seen:
                    image_copy[new_i][new_j] = color
                    q.append((new_i,new_j))
        return image_copy
        