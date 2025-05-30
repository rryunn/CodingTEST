import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        Queue<int[]> queue= new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        int[] dr = {1,0,-1,0};
        int[] dc  = {0,1,0,-1};
        
        queue.offer(new int[] {0,0,1});
        visited[0][0] = true;
        
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            int dist = cur[2];
            
            if(r==n-1 && c == m-1) return dist;
            for(int i =0 ;i<4 ; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if(nr>=0 && nr<n && nc>=0 && nc<m && maps[nr][nc]==1){
                    if(!visited[nr][nc]){
                        visited[nr][nc] = true;
                        queue.offer(new int[] {nr,nc,dist+1});
                    }
                }
            }
        }
        return -1;
        
    }
}