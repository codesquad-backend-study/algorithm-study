package programmers.fia.week6;

import java.util.*;

public class FiaCache {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) {
            return cities.length * 5;
        }

        int runtime = 0;

        Deque<String> cache = new ArrayDeque<>();

        for (String city : cities) {
            city = city.toLowerCase();
            if (cache.contains(city)) { // 캐시에 저장되어 있는 경우
                cache.remove(city);
                cache.addFirst(city);
                runtime += 1; // 실행 시간 1초
            } else { // 캐시에 저장되어 있지 않은 경우
                boolean isFull = cache.size() == cacheSize; // 캐시에 공간이 있는지 확인
                if (!isFull) { // 캐시 공간이 비어있는 경우
                    cache.addFirst(city);
                } else { // 캐시 공간이 가득 찬 경우
                    cache.removeLast(); // 가장 오래 전에 사용한 캐시 제거
                    cache.addFirst(city);// 새로 캐시 저장
                }
                runtime += 5; // 실행 시간 5초
            }
        }

        return runtime;
    }

    public static void main(String[] args) {
        int cacheSize =	2;
        String[] cities = {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"};
        FiaCache fiaCache = new FiaCache();
        fiaCache.solution(cacheSize, cities);
    }
}
