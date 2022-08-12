**c++**

```c++
class Solution {
public:
    void fillrow(vector<vector<int>>& matrix,int row,int col){
        for(int i =0;i<col;++i){
            matrix[row][i] =0;
        }
    }
    void fillcol(vector<vector<int>>& matrix,int row,int col){
        for(int i = 0;i<row;++i)
            matrix[i][col]=0;
    }
    
    void setZeroes(vector<vector<int>>& matrix) {
        int rowsize = matrix.size();
        int colsize = matrix[0].size();
        
        bool row[201];
        bool col[201];
        queue<pair<int,int>> q;
        memset(row,false,sizeof(row));
        memset(col,false,sizeof(col));

        for(int i = 0 ;i<rowsize;++i){
            for(int j = 0; j<colsize; ++j){
                if(matrix[i][j]==0 ){
                    q.push(make_pair(i,j));    
                }
            }
        }
        
        while(!q.empty()){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            if(row[x]==false){
                fillrow(matrix,x,colsize);
                row[x]=true;
            }
            if(col[y] == false){
                fillcol(matrix,rowsize,y);
                col[y] =true;
            }
        }
    }
};
```


**python**


```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowcheck = [False] * row
        colcheck = [False] * col
        dq =deque()
        for i in range(row):
            for j in range(col) : 
                if matrix[i][j] == 0 : 
                    dq.append((i,j))
        while dq : 
            x,y = dq.popleft()
            if rowcheck[x] != True : 
                matrix[x]= [0] * col
                print(matrix)
                rowcheck[x] = True
            if colcheck[y] != True:
                for k in range(row) : 
                    matrix[k][y] = 0
                colcheck[y] = True
                    
                
```