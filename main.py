"""
from MiYouShe import *

test = get_MiYouShe()
print(test.get_UID_MiYouShe_ys(75276539))
"""
import requests
import string

UID = 20934997
payload = {"uid": str(UID)}
cookies = {"DS": "1610096818,o21jnm,9bc9d36a6788ba0321110f1a42f452bd",
           "cookie": "stuid=20934997;stoken=F1Lk01HQpbMkphLe7vGZIOcuYWCv9VWT6JXOpyfN;",
           "x-rpc-client_type": "2",
           "x-rpc-app_version": "2.3.0",
           "x-rpc-sys_version": "11",
           "x-rpc-channel": "miyousheluodi",
           "x-rpc-device_id": "14ae08d4-8706-3728-9e96-45e6ea3b5b07",
           "x-rpc-device_name": "Xiaomi Redmi K30 Pro",
           "x-rpc-device_model": "Redmi K30 Pro",
           "Referer": "https://app.mihoyo.com",
           "Host": "api-takumi.mihoyo.com",
           "Connection": "Keep-Alive",
           "Accept-Encoding": "gzip",
           }
urls = "https://api-takumi.mihoyo.com/game_record/card/api/getGameRecordCard?uid=20934997"
MIYouShe_ys_json = requests.get(urls, headers=cookies)
MIYouShe_ys_json = MIYouShe_ys_json.json()
Ys_Game_ID = MIYouShe_ys_json["data"]["list"]["game_role_id"]
YS_Game_Name = MIYouShe_ys_json["data"]["list"]["nickname"]
Ys_Game_Region = MIYouShe_ys_json["data"]["list"]["region_name"]
Ys_Game_Leve = MIYouShe_ys_json["data"]["list"]["level"]
Ys_Game_Day = MIYouShe_ys_json["data"]["list"]["data"]["value"][0]
Ys_Game_role_num = MIYouShe_ys_json["data"]["list"]["data"]["value"][1]
Ys_Game_achi_num = MIYouShe_ys_json["data"]["list"]["data"]["value"][2]
Ys_Game_tower_num = MIYouShe_ys_json["data"]["list"]["data"]["value"][3]
result = "游戏内ID：" + Ys_Game_ID + "游戏内名称：" + YS_Game_Name + "服务器：" + Ys_Game_Region + "等级：" + Ys_Game_Leve + \
         "活跃天数：" + Ys_Game_Day + "拥有角色数量" + Ys_Game_role_num + "完成成就数：" + Ys_Game_achi_num + \
         "深境螺旋：" + Ys_Game_tower_num
