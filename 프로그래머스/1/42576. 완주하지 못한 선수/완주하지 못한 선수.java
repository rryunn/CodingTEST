import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> counter = new HashMap<>();
        
        for (String p : participant){
            counter.put(p, counter.getOrDefault(p,0)+1);
        }
        
        for (String c: completion){
            counter.put(c, counter.get(c)-1);
        }
        
        for(String key: counter.keySet()){
            if(counter.get(key)!=0){
                return key;
            }
        }
        return null;

    }
}