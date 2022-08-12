```c++
bool cmp(pair<string,int>& a,pair<string,int>& b)
{
    return a.first<b.first;
}
class Solution {
public:

    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<pair<string,int>> vec;
        vector<vector<string>> result;
        for(size_t i =0;i<strs.size();++i)
        {
            string temp = strs[i];
            sort(temp.begin(),temp.end());
            vec.push_back(make_pair(temp,i));
        }
        sort(vec.begin(),vec.end(),cmp);
        for(size_t i = 0; i<vec.size();++i)
        {
            vector<string> tempvec;
            tempvec.push_back(strs[vec[i].second]);
            while(i+1<vec.size() && vec[i+1].first == vec[i].first)
            {
                ++i;
                tempvec.push_back(strs[vec[i].second]);
            }
            result.push_back(tempvec);
        }
    
       return result;
    }
};
```

**python**

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            word = list(strs[i])
            word.sort()
            word = ''.join(word)
            if word not in dic : 
                dic[word] = deque()
                dic[word].append(strs[i])
            else : 
                dic[word].append(strs[i])
        res = []
        for i in dic:
            res.append(dic[i])
        return res
```