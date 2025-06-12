import java.util.*;
class Solution {
    public int[] solution(int[] num_list, int n) {
       // 배열에서 0번 인덱스부터 n번째 인덱스 바로 전까지 자르기
        return Arrays.copyOfRange(num_list, 0, n);
    
    }
}