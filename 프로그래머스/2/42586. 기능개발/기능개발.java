import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        int n = progresses.length;
        int[] left = new int[n];
        int[] days = new int[n];
        
        for(int i=0;i<n;i++){
            left[i] = 100-progresses[i];
            if(left[i]%speeds[i]!=0)
                days[i] = left[i]/speeds[i]+1;
            else
                days[i] = left[i]/speeds[i];
        }
        
        List<Integer> answer = new ArrayList<>();
        int prevDay = days[0];
        int count =1;
        for(int i=1;i<days.length;i++){
            if(days[i]<=prevDay){
                count++;
            }else{
                answer.add(count);
                count=1;
                prevDay = days[i];
            }
        }
        answer.add(count);
        
        int[] result = new int[answer.size()];
        for(int i=0;i<answer.size();i++){
            result[i] = answer.get(i);
        }
        return result;
        
    }
}