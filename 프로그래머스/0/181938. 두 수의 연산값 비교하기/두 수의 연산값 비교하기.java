class Solution {
    public int solution(int a, int b) {
        String total = Integer.toString(a) + Integer.toString(b);
        int total2 = Integer.parseInt(total);
        
        if(total2>=2*a*b){
            return total2;
        }else{
            return 2*a*b;
        }
    }
}