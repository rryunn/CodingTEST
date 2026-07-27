import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        ArrayList<Integer> list = new ArrayList<>();
        Deque<Integer> queue = new ArrayDeque<>();
        
        for(int i=0;i<progresses.length;i++){
            int check = (100-progresses[i])%speeds[i];
            if(check !=0)
                queue.add((100-progresses[i])/speeds[i] +1);
            else
                queue.add((100-progresses[i])/speeds[i]);
        }
        
        // [7,70,45]  -> [7,3,9]
        int count =1;
        int standard = queue.poll(); // 7 [3,9]
        while(!queue.isEmpty()){ 
            if(standard >= queue.peek()){
                count++;
            
                int trash = queue.poll(); // 패스하고 뒤의 값도 같이 할 수 있는지 봐야하니까
            }else{
                list.add(count);
                count =1;
                standard = queue.poll();
            }            
        }
        list.add(count);
        
        int[] answer = new int[list.size()];
        for(int i=0;i<answer.length;i++){
            answer[i] = list.get(i);
        }
        return answer;
        
    }
}