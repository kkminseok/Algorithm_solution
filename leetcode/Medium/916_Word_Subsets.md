**c++**

```c++
class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        string temp = "";
        int chrcount[26]={0,};
        for(size_t i =0;i<B.size();++i)
        {
            int subcount[26]={0,};
            for(size_t j =0;j<B[i].size();++j)
            {
                subcount[B[i][j]-97]++;
                chrcount[B[i][j]-97] = max(subcount[B[i][j]-97], chrcount[B[i][j]-97]);
            }
        }
        for(int i =0;i<26;++i)
        {
            while(chrcount[i]!=0)       
            {
                temp+=(i+97);
                chrcount[i]--;
            }
        }
        vector<string> result;
        sort(temp.begin(),temp.end());
        for(size_t i =0;i<A.size();++i)
        {
            bool check=true;
            string Atemp = A[i];
            sort(Atemp.begin(),Atemp.end());
            int subindex = 0;
            int j = 0;
            for(;j<temp.size() && subindex<Atemp.size();)
            {
                if(Atemp[subindex] == temp[j])
                {
                    ++subindex;
                    ++j;
                }
                else
                    subindex++;
            }
            if(j==temp.size())
                result.push_back(A[i]);
        }

        return result;
    }
    
};
```