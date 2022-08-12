**c++**

```c++
class UndergroundSystem {
    //stationName, id, time
    unordered_map<int,pair<string,int>> inmm;
    unordered_map<string,pair<int,int>> outmm;
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        inmm[id]= {stationName , t};
    }
    
    void checkOut(int id, string stationName, int t) {
        auto& it = inmm[id];
        string end = it.first + "-" + stationName;
        outmm[end].first += t - it.second;
        outmm[end].second +=1;
        
    }
    
    double getAverageTime(string startStation, string endStation) {
        string find = startStation + "-" + endStation;
        double result = double(outmm[find].first) / double(outmm[find].second);
        return result;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
 ```