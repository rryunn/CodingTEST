import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        //queue에 하나씩 넣으면서 제일 마지막에 넣은게 같으면 패스
        Deque<Integer> queue = new ArrayDeque<>();
        
        for(int i : arr){
            if(queue.isEmpty()){
                queue.add(i);
            }else{
                if(queue.peekLast() == i) continue;
                else
                    queue.add(i);
            }
        }
        
        int[] answer = new int[queue.size()];
        for(int i=0;i<answer.length;i++){
            answer[i]= queue.poll();
        }
        
        return answer;
    }
}