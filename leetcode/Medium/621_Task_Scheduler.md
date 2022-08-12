**c++**


```c++
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int> um;
        int count = 0 ; 
        for(size_t i =0 ;  i <tasks.size();++i){
            um[tasks[i]] ++;
            count = max(um[tasks[i]],count);
        }
        int res = (count -1) * (n+1);
        for(auto e : um){
            if(e.second == count) ++res;
        }
        if(tasks.size() >= res) res = tasks.size();
        return res;
    }
};
```