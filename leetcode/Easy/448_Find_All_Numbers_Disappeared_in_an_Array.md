```c++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result ;
        int size = nums.size();
        bool* check = new bool[nums.size()+1];
        memset(check,false,sizeof(bool) * (nums.size()+1));
        for(int i = 0;i<size;++i)
        {
            check[nums[i]]=true;
        }
        for(int i = 1;i<=size;++i)
        {
            if(check[i]==false)
                result.push_back(i);
        }
        
        
        return result;
    }
};
```