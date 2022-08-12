```c++
int MAP[101]={0,};
class Solution {
public:
    bool BFS(int start, vector<vector<int>>& graph)
    {
        queue<int> q;
        q.push(start);
        MAP[start] = 1;
        while (!q.empty())
        {
            int curr = q.front();
            q.pop();
            for (int i = 0; i < graph[curr].size(); ++i)
            {
                int ver = graph[curr][i];
                if (MAP[ver] != 0)//방문기록이 있음.
                {
                    if (MAP[curr] == MAP[ver])//색이 같다.
                    {
                        return false;
                    }
                }
                else
                {
                    q.push(ver);
                    MAP[ver] = 3 - MAP[curr];
                }
            }

        }
        return true;
    }

    
    
    bool isBipartite(vector<vector<int>>& graph) {
        bool result = true;
        memset(MAP,0,sizeof(MAP));
        for(size_t i =0;i<graph.size();++i)
        {
            if(MAP[i]==0)
            {
                result = BFS(i,graph);
                cout<<i<<" "<<result<<'\n';
                if(result==false)
                    return result;
                
            }
        }
        
        return result;
    }
};
```