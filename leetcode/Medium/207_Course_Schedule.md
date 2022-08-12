**c++**


```c++
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int>* graph = new vector<int>[numCourses+1];
        bool* check = new bool[sizeof(bool) * numCourses+1];
        for(size_t i =0;i<prerequisites.size();++i)
        {
            graph[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }
        
        //BFS
        for(int i = 0;i<numCourses;++i)
        {
            if(graph[i].size()==0)
                continue;
            else
            {
                fill(check,check+numCourses+1,false);
                queue<int> q;
                q.push(i);
                check[i]=true;
                while(!q.empty())
                {
                    int x = q.front();
                    //cout<<x<<'\n';
                    q.pop();
                    for(int k =0;k<graph[x].size();++k)
                    {
                        int temp = graph[x][k];
                        if(graph[temp].size()==0)
                            continue;
                        if(!check[graph[x][k]])
                        {
                            q.push(graph[x][k]);
                            check[graph[x][k]]=true;
                        }
                        if(graph[x][k]==i)
                        {
                            return false;
                        }
                    }
                }
                
            }
        }
        return true;
    }
};
```