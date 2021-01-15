from datetime import datetime, date, timedelta
train_start = datetime.strptime("01:39:27", "%H:%M:%S").time()
train_end = datetime.strptime("07:16:54", "%H:%M:%S").time()

print(type(timedelta(days=1)))
print(type(date.today()))
yesterday = date.today() - timedelta(days=1)
print(yesterday)
duration = datetime.combine(yesterday, train_end) - datetime.combine(yesterday, train_start)
print("time taken for training yolo model:", duration)