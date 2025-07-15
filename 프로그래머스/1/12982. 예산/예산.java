import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int count =0;
        Arrays.sort(d);
        for(int don : d){
            if(budget-don>=0){
                count++;
                budget = budget-don;
            }else{
                return count;
            }
        }
        return count;
    }
}