import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n];
        
        int answer =0;
        
        for(int i =0;i<n;i++){
            
            if(visited[i]) continue;
            answer++;
            
            queue.offer(i);
            visited[i] = true;
            
            while(!queue.isEmpty()){
                int cur = queue.poll();
                
                for(int j=0;j<n;j++){
                    if(computers[cur][j]==1 && !visited[j]){
                        queue.offer(j);
                        visited[j] = true;
                    }
                }
            }
        }
        return answer;
    }
}