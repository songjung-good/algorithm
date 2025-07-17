-- 코드를 입력하세요
SELECT FIRST_HALF.FLAVOR FROM FIRST_HALF
JOIN ICECREAM_INFO ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
WHERE ICECREAM_INFO.INGREDIENT_TYPE = 'fruit_based' and TOTAL_ORDER >= 3000
ORDER BY TOTAL_ORDER DESC;
    # FLAVOR in ('peach', 'watermelon', 'mango', 'strawberry', 'melon', 'orange', 'pineapple')
#