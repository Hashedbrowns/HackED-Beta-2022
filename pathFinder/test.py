# from datetime import datetime


# CALL_LIMIT = 500

# edges = [(i,0) for i in range(10000)]
# calls = {}
# start = datetime.now()

# while edges:
#     now = datetime.now()
#     cur_time = (now-start).seconds // 60
#     if cur_time not in calls:
#         calls[cur_time] = 0

#     if calls[cur_time] < CALL_LIMIT:
#         e = edges.pop()
#         print(f"[{cur_time}] processed: {e}")
#         calls[cur_time] += 1

import json
import polyline
import requests


req=requests.get("http://uofadirections.herokuapp.com/api/?start=CSC&end=CCIS&iweight=0.2")
print(req.headers)
# with open("route.json","r+") as rf    :
#     route=json.load(rf)


# for x in route["route"]:
#     pts=polyline.decode(x["polyline"])
#     print(pts)
