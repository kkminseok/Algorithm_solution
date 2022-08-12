**c++**

```c++
class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        
        set<string> st;
        for(int i = 0 ; i <words.size() ; ++i){
            for(int j = 0 ; j < words.size();++j){
                if(i==j) continue;
                if( words[j].find(words[i]) != -1){
                    st.insert(words[i]);
                    break;
                }
            }
        }
        vector<string> res(st.begin(),st.end());
        return res;    
    }
};
```