import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int count = numbers.length;
        int max1= numbers[count-1];
        int max2= numbers[count-2];
        return max1*max2;
    }
}