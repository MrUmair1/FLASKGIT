import requests

Base = "http://127.0.0.2:3308/"

# data = [{"name": "meeru", "views": 40000, "likes": 29},
#         {"name": "dhakkan", "views": 30000, "likes": 49},
#         {"name": "gooluu", "views": 60000, "likes": 59}]
#
#
#
# c = 1
# for i in data:
#     response = requests.put(Base + f"video/{c}", i)
#     c+=1
# print(response.json())
# # input()
response = requests.get(Base + "video/1")
# print(response.json())
#
# response = requests.delete(Base + "video/1")
# print(response)
# response = requests.patch(Base + "video/2")
# print(response.json())
# #
# input()
# response = requests.get(Base + "video/2")