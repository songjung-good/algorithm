from datetime import datetime, timezone

# 현재 UTC 시간 가져오기
current_time = datetime.now(timezone.utc)
# 날짜와 시간 구분하여 출력
current_date = current_time.date()

print(current_date.year)
print(current_date.month)
print(current_date.day)