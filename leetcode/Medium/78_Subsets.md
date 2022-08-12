**python**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.result = []
        self.solution(0,nums,[])
        return self.result
    
    def solution(self, depth : int, nums : List[int], temp : List[int]):
        if depth == len(nums):
            self.result.append(temp)
            return 
        temp.append(nums[depth])
        self.solution(depth+1,nums,temp[:])
        temp.pop()
        self.solution(depth+1,nums,temp[:])        
        
```

-----  

**c++**

```c++
class Solution {
public:
    void solution(vector<vector<int>>& vec,int depth,vector<int>& nums,vector<int> temp)
    {
        if(depth == nums.size())
        {
            vec.push_back(temp);
            return;
        }
        temp.push_back(nums[depth]);
        solution(vec,depth+1,nums,temp);
        temp.pop_back();
        solution(vec,depth+1,nums,temp);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        solution(result,0,nums,temp);
        return result;
    }
};
```