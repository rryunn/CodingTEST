-- 코드를 작성해주세요
SELECT F1.ID AS ID, F2.FISH_NAME AS FISH_NAME, F1.LENGTH AS LENGTH
FROM FISH_INFO AS F1 JOIN FISH_NAME_INFO AS F2 ON F1.FISH_TYPE = F2.FISH_TYPE
WHERE (F1.FISH_TYPE, F1.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH) FROM FISH_INFO WHERE LENGTH IS NOT NULL GROUP BY FISH_TYPE)
ORDER BY ID ASC;
