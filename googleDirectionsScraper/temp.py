from datetime import datetime


CALL_LIMIT = 500

calls = {}
start = datetime.now()

while edges:
    now = datetime.now()
    cur_time = (now-start).seconds // 60
    if cur_time not in calls:
        calls[cur_time] = 0

    if calls[cur_time] < CALL_LIMIT:
        e = edges.pop()
        print(f"[{cur_time}] processed: {e}")
        calls[cur_time] += 1
