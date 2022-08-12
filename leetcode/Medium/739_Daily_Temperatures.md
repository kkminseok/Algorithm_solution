**c++**

```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(),0);
        stack<pair<int,int>> st;
        
        for(size_t i = 0 ; i <T.size();++i){
            if(st.empty())st.push(make_pair(T[i],i));
            else{
                while(!st.empty() && st.top().first < T[i]){
                    int index = st.top().second;
                    res[index] = i - index;
                    st.pop();
                }
                st.push(make_pair(T[i],i));
            }
        }
        return res;
    }
};
```