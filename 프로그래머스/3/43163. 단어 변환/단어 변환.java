import java.util.*;

class Solution {
    boolean check(String begin, String word) {
        if (begin.length() != word.length()) {
            return false;
        }
        int diff = 0;
        for (int i = 0; i < word.length(); i++) {
            if (begin.charAt(i) != word.charAt(i)) {
                diff++;
            }
        }
        return diff == 1;
    }

    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) {
            return 0;  // target이 words에 없다면 바로 0 반환
        }

        Queue<String> queue = new LinkedList<>();
        boolean[] visited = new boolean[words.length];
        int count = 0;

        queue.offer(begin);

        while (!queue.isEmpty()) {
            int size = queue.size();  // 현재 레벨의 크기
            for (int i = 0; i < size; i++) {
                String current = queue.poll();

                if (current.equals(target)) {
                    return count;  // target을 찾으면 바로 리턴
                }

                for (int j = 0; j < words.length; j++) {
                    // 아직 방문하지 않았고, 단어 하나만 다르면
                    if (!visited[j] && check(current, words[j])) {
                        queue.offer(words[j]);
                        visited[j] = true;  // 방문 표시
                    }
                }
            }
            count++;  // 한 레벨이 끝날 때마다 증가
        }

        return 0;  // target을 못 찾은 경우 0 반환
    }
}
