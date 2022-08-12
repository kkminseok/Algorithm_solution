**c++**

```c++
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};
class Solution {
public:
    
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        vector<bool> v(col,false);
        vector<vector<bool>> vc;
        vector<int> res;
            
        for(int i = 0 ; i<row;++i)
            vc.push_back(v);

        
        queue<pair<int,int>> q;
        q.push(make_pair(0,0));
        vc[0][0] = true;
        int dis = 0;
        int count = 0;
        while(!q.empty()){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            res.push_back(matrix[x][y]);
            ++count;
            if(count== row * col) break;
            
            int newX = x + dx[dis];
            int newY = y + dy[dis];
            
            if(newX <0 || newX >= matrix.size() || newY <0 || newY >= matrix[0].size() ||vc[newX][newY]){
              dis = (dis+1)%4;
                newX = x + dx[dis];
                newY = y +dy[dis];
            } 
            if(!vc[newX][newY]){
                q.push(make_pair(newX,newY));
                vc[newX][newY] = true;
            }
        }
        
        return res;
    }
};
```