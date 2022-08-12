**c++**

```c++
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};
bool v[151][151]={false,};
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
     //BFS
        if(matrix.size()==0)
            return matrix;
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> result;
        
        for(int i =0 ; i < row;++i)
        {
            for(int j = 0;j<col;++j)
            {
                bool pc = false;
                bool ac = false;
                //BFS
                memset(v,false,sizeof(v));
                //Pacific
                queue<pair<int,int>> pacific;
                pacific.push(make_pair(i,j));
                while(!pacific.empty())
                {
                    int x = pacific.front().first;
                    int y = pacific.front().second;
                    //cout<<"x"<<x<<"y"<<y<<'\n';
                    if(x==0||y==0)
                    {
                        pc=true;
                    }
                    if(x==row-1 || y==col-1)
                    {
                        ac=true;
                    }
                    if(pc && ac)
                    {
                        //cout<<"pc  ac\n";
                        vector<int> temp;
                        temp.push_back(i);
                        temp.push_back(j);
                        result.push_back(temp);
                        break;
                    }
                    pacific.pop();
                    for(int k = 0;k<4;++k)
                    {
                        int newX = x + dx[k];
                        int newY = y + dy[k];
                        if(0<=newX && newX<row && 0<=newY && newY<col && matrix[newX][newY]<=matrix[x][y] && !v[newX][newY])
                        {
                            v[newX][newY]=true;
                            pacific.push(make_pair(newX,newY));
                        }
                    }
                }
            }
        }
        return result;
    }
};
```