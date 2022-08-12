```c++
const int MAX = 101;

bool v[MAX][MAX]={false};
int MAP[MAX][MAX];

int dx[8]={-1,1,1,-1,-1,0,1,0};
int dy[8]={1,1,-1,-1,0,1,0,-1};

class Solution {
public:
    int BFS(vector<vector<int>>& grid,int _size)
    {
        memset(v,false,sizeof(v));
        int size = _size;
        //x y count
        queue<pair<pair<int,int>,int>> q;
        q.push(make_pair(make_pair(0,0),1));
        v[0][0]=true;
        while(!q.empty())
        {
		    int x = q.front().first.first;
		    int y = q.front().first.second;
		    int count = q.front().second;
            if(x == (size-1) && y ==(size-1))
                return count;
            q.pop();
            for(int k=0;k<8;++k)
            {
                int newX = x + dx[k];
                int newY = y + dy[k];

                if(0<=newX && newX<size && 0<=newY && newY<size && grid[newX][newY]==0 && !v[newX][newY])
                {
                    q.push(make_pair(make_pair(newX,newY),count+1));
                    v[newX][newY]=true;
                }
            }
        }
        return -1;
    }
    
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if(grid[0][0]==1)
            return -1;
        int result =BFS(grid,grid.size());
        return result;
    }
};
```