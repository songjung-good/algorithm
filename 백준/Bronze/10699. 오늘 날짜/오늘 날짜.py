from datetime import datetime

# 현재 날짜를 YYYY-MM-DD 형식으로 출력
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
print(current_date)
