```c++
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(size_t i =0;i<s.size();++i)
        {
            if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            {
                st.push(s[i]);
            }
            else
            {
                if(st.empty())
                    return false;
                else
                {
                    char temp = st.top();
                    st.pop();
                    if(s[i]==')' && temp!='(')
                        return false;
                    else if(s[i]==']' && temp!='[')
                        return false;
                    else if(s[i]=='}' && temp!='{')
                        return false;       
                }
            }
        }
        if(st.empty())
            return true;
        else
            return false;
    }
};
```