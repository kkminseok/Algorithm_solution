**c++**

```c++
class Solution {
    bool v[301][301]={false,};
    int dx[4] ={0,-1,1,0};
    int dy[4] = {1,0,0,-1};
public:
    int BFS(int i,int j,int row,int col,vector<vector<char>>& grid)
    {
        queue<pair<int,int>> q;
        q.push(make_pair(i,j));
        v[i][j]=true;
        
        while(!q.empty())
        {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            for(int k =0;k<4;++k)
            {
                int newX = x+dx[k];
                int newY = y+dy[k];
                if(0<=newX && newX<row && 0<=newY && newY<col && !v[newX][newY] && grid[newX][newY]=='1')
                {
                    v[newX][newY] = true;
                    q.push(make_pair(newX,newY));
                }
            }
        }
        return 1;
    }
    int numIslands(vector<vector<char>>& grid) {
        int result = 0;
        memset(v,false,sizeof(v));
        int row = grid.size();
        int col = grid[0].size();
        for(size_t i =0;i<row;++i)
        {
            for(size_t j = 0 ;j<col;++j)
                if(grid[i][j] == '1'&&!v[i][j])
                    result += BFS(i,j,row,col,grid);
        }
        return result;
    }
};
```