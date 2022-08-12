**python**

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        dq = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0 :
                    dq.append((i,j))
                else : 
                    mat[i][j] = 987654321
        while dq : 
            x,y = dq.popleft()
            for k in range(4):
                newx,newy = x + dx[k] , y + dy[k]
                z = mat[x][y]+1 
                if 0 <= newx and newx < row and 0 <= newy and newy < col and mat[newx][newy] > z :
                    mat[newx][newy] = z
                    dq.append((newx,newy))
        return mat
    
    
```