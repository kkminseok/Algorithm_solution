**python**

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        v = []
        for i in range(m) : 
            v.append([])
            for j in range(n) :
                v[i].append([])
        for i in range(m):
            for j in range(n):
                if i == 0 or j ==0 : 
                    v[i][j] = 1 
                else : 
                    v[i][j] = v[i-1][j] + v[i][j-1]
        return v[m-1][n-1]
```

-----  

**c++**

```c++
class Solution {
public:
    void cal(int m,int n,int** map)
    {
        for(int x =1;x < m ;++x)   
        {
            for(int y = 1; y<n;++y)
            {
                map[x][y] = map[x-1][y] + map[x][y-1];
            }
        }
    }
    
    int uniquePaths(int m, int n) {
        int** map = new int*[m];
        for(int i =0;i<m;++i)
            map[i] = new int[n];
        for(int i=0;i<m;++i)
        {
            for(int j =0;j<n;++j)
            {
                map[i][j]=1;
            }
        }
        cal(m,n,map);
        int result = map[m-1][n-1];
        for(int i =0;i<m;++i)
        {
            delete []map[i];
        }
        delete[] map;
        return result;
    }
};
```