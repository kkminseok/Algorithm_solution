**c++**

```c++
class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> words(wordlist.begin(),wordlist.end());
        unordered_map<string,string> lowerlist,vowlist;
        for(string w : wordlist){
            string lowword = makelow(w),  vowword = makevow(w);
            lowerlist.insert({lowword,w});
            vowlist.insert({vowword,w});
        }
        
        for(size_t i =0;i<queries.size();++i)
        {
            if(words.count(queries[i]))continue;
            string lowq = makelow(queries[i]), vowq = makevow(queries[i]);
            if(lowerlist.count(lowq))
                queries[i] = lowerlist[lowq];
            else if(vowlist.count(vowq))
                queries[i] = vowlist[vowq];
            else
                queries[i] = "";
        }
        return queries;
    }
    string makelow(string w){
        for(auto& c : w){
            c = tolower(c);
        }
        return w;
    }
    string makevow(string w){
        w= makelow(w);
        for(auto&c : w){
            if(c =='a'||c=='e'||c=='i'||c=='o'||c=='u')
                c='#';
        }
        return w;
    }
};
```