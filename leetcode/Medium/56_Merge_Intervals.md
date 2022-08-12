**python**

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result =[]
        intervals.sort()
        index = 0
        while index < len(intervals):
            temp = []
            start = intervals[index][0]
            end = intervals[index][1]
            j = index+1
            while j < len(intervals) and end >= intervals[j][0] : 
                end = max(intervals[j][1],end)
                index = j
                j += 1
            temp.append(start)
            temp.append(end)
            result.append(temp)
            index+=1
        return result
        
```

-----  

**c++**

```c++
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        sort(intervals.begin(),intervals.end());
        for(int i = 0; i<intervals.size(); ++i)
        {
            vector<int> temp;
            int start = intervals[i][0];
            int end = intervals[i][1];
            int j = i+1;
            while(j<intervals.size() && end >= intervals[j][0])
            {
                end = max(intervals[j][1],end);
                i=j;
                ++j;
            }
            temp.push_back(start);
            temp.push_back(end);
            result.push_back(temp);
        }
        
        return result;
    }
};
```