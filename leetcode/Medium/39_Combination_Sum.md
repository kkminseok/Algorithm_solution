```c++
class Solution {
public:
    vector<vector<int>> result;
    void practice(vector<int>& candidates, int target,vector<int> temp,int num)
    {
        if(target==0)
        {
               result.push_back(temp);
        }
        else if(target<0)
        {
            return;
        }
        else
        {
            for( ;num<candidates.size();++num)
            {
                temp.push_back(candidates[num]);
                practice(candidates,target-candidates[num],temp,num);
                temp.pop_back();
            }
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        practice(candidates,target,temp,0);
        return result;
    }
};
```