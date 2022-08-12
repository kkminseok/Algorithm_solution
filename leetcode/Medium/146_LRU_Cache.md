**c++**

```c++
class LRUCache {
    typedef unordered_map<int,pair<int,list<int>::iterator>> UMIL;
    UMIL cache;
    list<int> result;
    int _size;
public:
    LRUCache(int capacity) {
        _size = capacity;
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if(it!=cache.end())
        {
            move(it);
            return it->second.first;
        }
        else
            return -1;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if(it!=cache.end())
        {
            //수정
            move(it);
        }
        else
        {
            if(_size == cache.size())
            {
                cache.erase(result.back());
                result.pop_back();
            }
            result.push_front(key);
        }
        cache[key] = {value, result.begin()};
            
    }
    void move(UMIL::iterator it)
    {
        int key = it->first;
        result.push_front(key);
        result.erase(it->second.second);
        it->second.second = result.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```