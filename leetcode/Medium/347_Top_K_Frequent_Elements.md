**c++**

```c++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> um;
        for(size_t i = 0 ; i<nums.size();++i)
            um[nums[i]]++;
        vector<int> res;
        
        priority_queue<pair<int,int>> pq;
        
        for(auto it = um.begin(); it!=um.end(); ++it){
            pq.push(make_pair(it->second,it->first));
            if(pq.size() > (int)um.size() - k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        
        return res;
    }
};
```