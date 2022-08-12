```c++
class Solution {
public:
    vector<int> findindex;
    int abs(int x)
    {
        return x <0 ? -x : x;
    }
    vector<int> shortestToChar(string s, char c) {
        
        vector<int> result;
        for(size_t i =0;i<s.size();++i)   
        {
             if(s[i]==c)
                 findindex.push_back(i);
        }
        int i = 0;
        int temp;
        for(int j = 0; j<s.size() && i<findindex.size();++j)
        {
            if(i+1 <findindex.size() &&  abs(findindex[i]-j)>abs(findindex[i+1]-j) )
                ++i;
            if(i+1<findindex.size())
                temp= min(abs(findindex[i]-j),abs(findindex[i+1]-j));
            else
                temp = abs(findindex[i]-j);
            result.push_back(temp);
        }
        
        return result;
    }
    
};
```