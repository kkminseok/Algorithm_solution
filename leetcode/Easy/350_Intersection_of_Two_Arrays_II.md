**c++**

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> um1;
        unordered_map<int,int> um2;
        vector<int> res;
        for(size_t i = 0 ; i< nums1.size();++i)
            um1[nums1[i]]++;
        for(size_t i = 0 ; i <nums2.size();++i)
            um2[nums2[i]]++;
        
        for(auto it = um1.begin(); it!=um1.end(); ++it){
            if(um1.count(it->first) && um2.count(it->first)){
                int count = min(um1[it->first] , um2[it->first]);
                for(int i = 0; i <count;++i)
                    res.push_back(it->first);
            }
        }
        return res;
    }
};
```