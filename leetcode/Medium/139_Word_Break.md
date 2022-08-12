**c++**

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        bool* v = new bool[s.size()+1];
        memset(v,false,sizeof(bool) *(s.size()+1) );
        v[0] = true;
        unordered_map<string,bool> map;
        for(size_t i =0;i<wordDict.size();++i)
        {
            map[wordDict[i]] = true;
        }
        for(int i =1;i<s.size()+1;++i)
        {
            for(int j =0;j<i;++j)
            {
                string temp(s,j,i-j);
                if(v[j] == true)
                {
                    auto it = map.find(temp);
                    if(it!=map.end())
                    {
                        v[i]=true;
                        break;
                    }
                }
            }
        }
        return v[s.size()];
    }
};
```

-----  

**python**

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        v = [0] * (len(s)+1)
        v[0]=1
        for i in range(1,len(s)+1):
            for j in range(i) : 
                if v[j] ==1 and s[j:i] in wordDict:
                    v[i] = 1
                    break
        if v[len(s)] == 1:
            return True
        return False
            
```