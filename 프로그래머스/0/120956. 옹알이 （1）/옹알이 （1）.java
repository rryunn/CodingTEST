class Solution {
    public int solution(String[] babbling) {
        
        int answer=0;
        String[] words = {"aya","ye","woo","ma"};
        
        for(String s: babbling){
            for(String word: words){
                s = s.replace(word," ");
            }
            
            s = s.replace(" ", "");
            
            if(s.isEmpty()){
                answer++;
            }
        }
        return answer;
    }
}