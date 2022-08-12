**python**

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sh = set()
        if k> len(s):
            return False
        
        for i in range(len(s)-k+1):
            temp = str()
            for j in range(k):
                temp +=s[i+j]
            sh.add(temp)
        if len(sh) == pow(2,k):
            return True
        return False
        
        
        
```

------

**c++**

```c++
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> sh;
        if(k>s.size())
            return false;
        
        for(int i=0;i<=s.size()-k;++i)
        {
            string temp = "";
            for(int j =0;j<k;++j)
            {
                temp+=s[i+j];
            }
            //cout<<temp<<" "<<sh.size()<<'\n';
            sh.insert(temp);
        }
        
        if(sh.size() == pow(2,k))
            return true;
        
        return false;
    }
};
```