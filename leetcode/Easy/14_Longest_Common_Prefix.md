**c++**

```c++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0)
            return "";
        
        string result="";
        bool ok = false;
        int count = 0; 
        while(!ok)
        {

            char standard;
            if(count < strs[0].size())
                standard = strs[0][count];
            for(size_t i =0;i<strs.size();++i)
            {
                if(strs[i][count]!=standard || count>= strs[i].size())
                {
                    ok=true;
                    break;
                }

            }
            if(!ok)
            {
                ++count;
                result+=standard;
            }
        }
        return result;
    }
};
```