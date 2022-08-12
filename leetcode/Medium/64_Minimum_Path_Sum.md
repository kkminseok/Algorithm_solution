**python**

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(1,row):
            grid[i][0] += grid[i-1][0]
        for j in range(1,col):
            grid[0][j] += grid[0][j-1]
        for i in range(1,row) :
            for j in range(1,col):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[row-1][col-1]
```        

-----  

**c++**

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        for(size_t i = 1;i<row; ++i)
            grid[i][0] += grid[i-1][0];
        for(size_t j = 1; j<col; ++j)
            grid[0][j] += grid[0][j-1];
        
        int i = 1;
        int j = 1;
        for(; i<row;++i)
        {
            for(j=1; j<col; ++j)
                grid[i][j] += (min(grid[i-1][j], grid[i][j-1]));
        }
        
        return grid[row-1][col-1];
    }
};
```