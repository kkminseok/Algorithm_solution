**c++**

```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(haystack.empty()&& needle.empty())return 0;
        else if(!haystack.empty() && needle.empty())return 0;
        
     return KMP(haystack,needle);
    }
    vector<int> maketable( string pattern)
    {
        int parttsize = pattern.size();
        vector<int> table(parttsize,0);
        int j  =0;
        for(int i =1;i<pattern.size();++i)
        {
            while(j>0 && pattern[i] != pattern[j])
            {
                j = table[j-1];
            }
            if(pattern[i] == pattern[j])
                table[i] = ++j;
        }
        return table;
    }
    
    int KMP(string origin, string pattern)
    {
        vector<int> table = maketable(pattern);
        int originsize = origin.size();
        int pattsize= pattern.size();
        int j =0;
        for(int i =0;i<origin.size();++i)
        {
            while(j> 0 && origin[i] != pattern[j])
                j = table[j-1];
            if(origin[i] == pattern[j])
            {
                if(j==pattsize-1)
                    return i - pattsize + 1;
                else
                    ++j;
            }
        }
        return -1;
    }
};
```