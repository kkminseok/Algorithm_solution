**c++**

```c++
class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        unordered_map<int,long long> um;
        for(size_t i = 0;i<arr.size();++i)
            um[arr[i]]++;
        
        long long result=0;
        
        for(auto it : um)
        {
            for(auto it2: um)
            {
                int first =it.first;
                int second = it2.first;
                int third = target-first-second;
                if(!um.count(third))continue;
                
                if(first == second && second== third)
                    result += um[first]* (um[first]-1) * (um[first]-2) / 6;
                else if(first==second && second!=third)
                    result += (um[first] * (um[first]-1))/2 * um[third];
                else if(first<second && second<third)
                    result += um[first] * um[second] * um[third];
                
            }
        }
        return (result %(int)(1e9+7));
    }
};


```