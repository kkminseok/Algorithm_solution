**c++**

```c++
class Trie {
public:
    /** Initialize your data structure here. */
    unordered_map<string,int> um;
    unordered_map<string,int> preum;
    Trie() {

    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        um[word]=  1;
        string temp = "";
        for(size_t i = 0;i<word.size();++i)
        {
            temp += word[i];
            preum[temp] = 1;
        }
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto it = um.find(word);
        if(it==um.end())
            return false;
        return true;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto it = preum.find(prefix);
        if(it==um.end())
            return false;
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```