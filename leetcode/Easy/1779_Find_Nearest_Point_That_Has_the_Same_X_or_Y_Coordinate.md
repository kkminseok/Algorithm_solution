**python**

```python
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        mind = 987654321
        for i in range(len(points)) : 
            if mind == 0 : 
                break
            x_d = x - points[i][0]
            y_d = y - points[i][1]
            
            if x_d != 0 and y_d !=0:
                continue
            distance = abs(x_d) + abs(y_d)
            if distance < mind:
                ans = i
                mind = distance
                
        return ans
```

**c++**
        
```c++
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int ans = -1;
        int mind = INT_MAX;
        for(size_t i =0;i<points.size() && mind != 0;++i)
        {
            int x_d = x - points[i][0];
            int y_d = y - points[i][1];
            
            if(x_d != 0 && y_d !=0)
            {
                continue;
            }
            int distance = abs(x_d) + abs(y_d);
            if(distance < mind)
            {
                ans = i;
                mind = distance;
            }
            
        }
        
        return ans;
    }
};
```