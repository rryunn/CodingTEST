import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n];
        int answer =0;
        for(int i=0;i<n;i++){
            
            if(visited[i]) continue;
            answer++;
            
            queue.offer(i);
            visited[i] = true;
            
            while(!queue.isEmpty()){
                int now = queue.poll();
                for(int next =0;next<n;next++){
                    if(computers[now][next] == 1 && !visited[next]){
                        queue.offer(next);
                        visited[next] = true;
                    }
                }
            }
        }
        return answer;
    }
}