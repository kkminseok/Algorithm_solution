```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        bool* v = new bool[nums.size()];
        memset(v,false,sizeof(bool) * nums.size());
        v[0]=true;
        for(size_t i =0;i<nums.size()-1;++i)
        {
            if(v[i]==true)
            {
                for(int j =0;j<=nums[i]; ++j)
                {
                    if(i+j>nums.size()-1)
                    {
                        break;
                    }
                    if(v[i+j]==true)
                        continue;
                    else
                        v[i+j]=true;
                }
            }
        }
        return v[nums.size()-1];
    }
};
```