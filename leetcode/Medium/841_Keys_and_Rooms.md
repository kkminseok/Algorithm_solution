**c++**

```c++
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        bool check[3001]={false,};
        check[0]=true;
        //bfs
        queue<int> q;
        q.push(0);
        while(!q.empty())
        {
            int x = q.front();
            q.pop();
            for(int k = 0;k<rooms[x].size();++k)
            {
                if(!check[rooms[x][k]])
                {
                    check[rooms[x][k]]=true;
                    q.push(rooms[x][k]);
                }
            }
        }
        for(size_t i =0;i<rooms.size();++i)
        {
            if(!check[i])
                return false;
        }
        return true;
    }
};
```