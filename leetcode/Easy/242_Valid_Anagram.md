```c++
class Solution {
public:
    int alpha[26]={0,};
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size())
            return false;
            
        for(size_t i=0;i<s.size();++i)
        {
            alpha[s[i]-97]++;
        }
        for(size_t i=0;i<t.size();++i)
        {
            if(alpha[t[i]-97]-1 <0)
                return false;
            alpha[t[i]-97]--;
        }
        return true;
    }
};
```