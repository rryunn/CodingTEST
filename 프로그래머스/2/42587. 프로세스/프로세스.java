import java.util.*;
class Solution {
    
    private int max_priority(Deque<int[]> max_pr){
        //우선순위 제일 큰거 찾는 함수
        int max = Integer.MIN_VALUE;
        for(int[] arr : max_pr){
            if(arr[0]>max){
                max=arr[0];
            }
        }
        return max;
    }
    public int solution(int[] priorities, int location) {
        //배열로 저장하니까 deque 자료형도 int[]로 해야지
        Deque<int[]> queue = new ArrayDeque<>();
        
        for(int i=0;i<priorities.length;i++){
            // [1,2]로 바로 넣을 수 없음. int[] 꼴로 선언하고 저장해줘야함.
            queue.add(new int[] {priorities[i],i}); //[(2,0),(1,1),(3,2),(2,2)]
        }
        
        int max_pr = max_priority(queue);
        int count =0;
        while(!queue.isEmpty()){
            if(queue.peek()[1]==location && queue.peek()[0]==max_pr){
                count = count+1;
                break;
            }
            if (queue.peek()[0]==max_pr){
                int[] trash = queue.poll();
                max_pr = max_priority(queue);
                count++;
            }else{
                int[] c = queue.poll();
                queue.add(c);
            }
        }
        return count;
        
        
    }
}