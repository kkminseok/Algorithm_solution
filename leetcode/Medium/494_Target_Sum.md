**c++**

```c++
class Solution {
public:
    void DFS(vector<int>& nums,int target,int curr,int index,int& result){
        if(index == nums.size()){
            if(curr == target)
                ++result;    
            return ;
        }
        DFS(nums,target,curr-nums[index],index+1,result);
        DFS(nums,target,curr + nums[index],index+1,result);
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        //DFS
        int result = 0 ;
        DFS(nums,target,0,0,result);
        return result;
    }
};
```