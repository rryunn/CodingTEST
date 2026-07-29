import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for(int i=1;i<=n;i++){
            graph.put(i, new ArrayList<>());
        }
        
        for(int[] e: edge){
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        
        Deque<int[]> queue= new ArrayDeque<>();
        boolean[] visited = new boolean[n+1];
        
        queue.offer(new int[] {1,0});
        visited[1] = true;
        
        int count =0;
        int maxDist = 0;
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int dist = cur[1];
            int node = cur[0];
            
            if(maxDist<dist){
                maxDist= dist;
                count = 1;
            }else if(maxDist == dist) count++;
            
            for(int next: graph.get(node)){
                if(visited[next]) continue;
                
                visited[next] = true;
                queue.offer(new int[] {next, dist+1});
            }
        }
        return count;
    }
}