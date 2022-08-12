```c++
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int pi=0;
        int popi=0;
        for(;popi<popped.size();)
        {
            if(st.empty())
                st.push(pushed[pi++]);
            while(st.top()!=popped[popi] && pi<pushed.size())
            {
                st.push(pushed[pi++]);
            }
            if(st.top()!=popped[popi])
                return false;
            st.pop();
            ++popi;
        }
        return true;
    }
};
```