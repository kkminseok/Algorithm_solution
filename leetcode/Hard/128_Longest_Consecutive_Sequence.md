**c++**

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        
        set<int> st;
        int count =1;
        for(size_t i = 0;i<nums.size();++i){
            st.insert(nums[i]);
        }
        if(st.size()==1) return 1;
        int num = INT_MAX;
        int temp = 0;
        int answer = 1;
        for(auto it = st.begin(); it!=st.end();++it)
        {
            if(num==INT_MAX){num = *it; continue;}
            else{
                temp = num;
                num = *it;
                if(temp+1 != num) {
                    count=1;
                    continue;
                }
                ++count;
                answer = max(answer, count);
            }
            
        }
        
        return answer;
    }
};
```