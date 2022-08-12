# C++

```c++
#include<unordered_map>
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> map;
        map.insert(make_pair('I',1));
        map.insert(make_pair('V',5));
        map.insert(make_pair('X',10));
        map.insert(make_pair('L',50));
        map.insert(make_pair('C',100));
        map.insert(make_pair('D',500));
        map.insert(make_pair('M',1000));        
        int result = 0;
        if(s.size()==1)
        {

            return (map.find(s[0])->second);
        }
        else
        {
            result = map.find(s[s.size()-1])->second;
            for(int i = s.size()-2; i > -1;--i)
            {
                int find = map.find(s[i+1])->second;
                int now = map.find(s[i])->second;
                if(find<=now)
                {
                    result+=now;
                }
                else
                    result-=now;
                
            }
            
        }
     return result;   
    }
};
```
