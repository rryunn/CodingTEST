import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        //s.charAt(index)
        //차이가 하나인지 보기
        Deque<Node> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[words.length];
        
        // begin 을 queue 에 넣고
        queue.offer(new Node(begin,0));

        while(!queue.isEmpty()){
            Node cur = queue.poll(); 
            String s = cur.word;
            int dist = cur.dist;
            if(s.equals(target)) return dist;
            
            for(int i=0;i<words.length;i++){
                
                int diff =0;
                if(!visited[i]){
                    for(int j=0;j<s.length();j++){
                        if(s.charAt(j)!=words[i].charAt(j)) diff++;
                    }

                    if (diff==1){
                        queue.offer(new Node(words[i], dist+1));
                        visited[i] = true;
                    }
                }

            }
        }
        return 0;       
    }
    class Node{
        String word;
        int dist;
        
        Node(String word, int dist){
            this.word = word;
            this.dist = dist;
        }
    }
}