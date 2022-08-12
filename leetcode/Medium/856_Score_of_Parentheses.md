```c++
class Solution {
public:
    int scoreOfParentheses(string S) {
        int result = 0;
        int count = 0;
        bool check  = false;
        for(size_t i = 0;i<S.size();++i)
        {
            if(S[i] == '(')
            {
                ++count;
                check=true;
            }
            else if (S[i]==')' && check)
            {
                result += pow(2,count-1);
                --count;
                check=false;
            }
            else
            {
                --count;
            }
        }
        return result;
    }
};
```