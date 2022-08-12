```c++
class Solution {
public:
    
    string findLongestWord(string s, vector<string>& dictionary) {
        string result = "";
        int sz= 0;
        sort(dictionary.begin(),dictionary.end());
        for(size_t i =0;i<dictionary.size();++i)
        {
            int index = 0;
            if(dictionary[i].size()>sz)
            {
                for(size_t j = 0; j<s.size();++j)
                {
                    if(dictionary[i][index]==s[j])
                    {
                        ++index;
                    }
                    if(index == dictionary[i].size())
                    {
                        sz = index;
                        result = dictionary[i];
                    }
                }
            }
        }
        return result;
        
    }
};
```