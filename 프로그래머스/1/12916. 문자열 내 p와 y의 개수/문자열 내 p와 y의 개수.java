class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p=0;
        int y=0;
        
        s = s.toLowerCase(); //다 소문자로.
        for (int i=0; i<s.length(); i++){
            if(s.charAt(i)=='p') p++;
            else if(s.charAt(i)=='y')y++;
        }
        if (p!=y) return false;
        return answer;
    }
}