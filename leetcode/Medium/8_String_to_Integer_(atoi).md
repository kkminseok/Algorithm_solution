**c++**



```c++
class Solution {
public:
    int myAtoi(string s) {
        if(s[0]>96 && s[0]<123 || s[0]=='.')
            return 0;
        if(s[0]==' ')
        {
            int i = 0;
            while(i<s.size() && s[0]==' ')
            {
                s = s.substr(1);
            }
        }
        int result;
        try
        {
        result = std::stoi(s);
        }
        catch(invalid_argument& e)
        {
            return 0;
        }
        catch(std::out_of_range& e)
        {
            if(s[0]=='-')
                result = -2147483648;
            else
                result = 2147483647;
        }
        return result;
    }
};
```


