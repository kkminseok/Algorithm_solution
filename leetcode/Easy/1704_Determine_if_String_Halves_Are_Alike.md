**c++**

```c++
class Solution {
public:
    bool halvesAreAlike(string s) {
        string a,b;
        set<char> st;
        st.insert('a');
        st.insert('e');
        st.insert('i');
        st.insert('o');
        st.insert('u');
        a = s.substr(0,s.size()/2);
        b = s.substr(s.size()/2);
        int aj = 0;
        int bj = 0;
        for(size_t i = 0 ;i<a.size();++i){
            if(st.count(tolower(a[i])))++aj;
            if(st.count(tolower(b[i])))++bj;
        }
        return aj==bj;
    }
};
```