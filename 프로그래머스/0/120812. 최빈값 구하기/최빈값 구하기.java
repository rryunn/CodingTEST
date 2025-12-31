import java.util.*;

class Solution {
    public int solution(int[] array) {

        Map<Integer, Integer> map = new HashMap<>();

        // 1. 빈도수 계산
        for (int key : array) {
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        int maxCount = 0;
        int answer = -1;
        boolean duplicated = false;

        // 2. 최빈값 찾기
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int key = entry.getKey();
            int count = entry.getValue();

            if (count > maxCount) {
                maxCount = count;
                answer = key;
                duplicated = false;
            } else if (count == maxCount) {
                duplicated = true;
            }
        }

        // 3. 여러 개면 -1
        return duplicated ? -1 : answer;
    }
}
