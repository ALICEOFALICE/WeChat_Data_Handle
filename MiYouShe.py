import random
import string
import time

import requests


class get_MiYouShe:
    def __init__(self):
        self.cookie = ""
        self.headers = {"user_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Geck\
        o) Chrome/81.0.4044.113 Safari/537.36"}

    def get_ds(self):
        # v2.3.0-web @povsister & @journey-ad
        n = 'h8w582wxwgqvahcdkpvdhbh2w9casgfl'
        i = str(int(time.time()))
        r = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
        c = self.hexdigest('salt=' + n + '&t=' + i + '&r=' + r)
        return '{},{},{}'.format(i, r, c)

    def get_Header(self):
        headers = {"DS": +self.get_ds(),
                   "cookie": "stuid=20934997;stoken=F1Lk01HQpbMkphLe7vGZIOcuYWCv9VWT6JXOpyfN;",
                   "x-rpc-client_type": "2",
                   "x-rpc-app_version": "2.3.0",
                   "x-rpc-sbh3_version": "11",
                   "x-rpc-channel": "miyousheluodi",
                   "x-rpc-device_id": "14ae08d4-8706-3728-9e96-45e6ea3b5b07",
                   "x-rpc-device_name": "Xiaomi Redmi K30 Pro",
                   "x-rpc-device_model": "Redmi K30 Pro",
                   "Referer": "https://app.mihoyo.com",
                   "Host": "api-takumi.mihoyo.com",
                   "Connection": "Keep-Alive",
                   "Accept-Encoding": "gzip",
                   }
        return headers

    def get_UID_MiYouShe_info(self, UID):
        urls = "https://bbs-api.mihoyo.com/user/wapi/getUserFullInfo?gids=2&uid=" + str(UID)
        MIYouShe_info_json = requests.get(urls, headers=self.headers)
        UID_name = (MIYouShe_info_json.json())["data"]["user_info"]["nickname"]
        UID_introduce = ((MIYouShe_info_json.json())["data"]["user_info"]["introduce"])
        UID_follower = (MIYouShe_info_json.json())["data"]["user_info"]["achieve"]["followed_cnt"]
        if (MIYouShe_info_json.json())["data"]["user_info"]["certification"]["type"] == 1:
            UID_label = (MIYouShe_info_json.json())["data"]["user_info"]["certification"]["label"]
        else:
            UID_label = "无可用认证"
        UID_like = (MIYouShe_info_json.json())["data"]["user_info"]["achieve"]["like_num"]
        UID_LEVEL_dby = (MIYouShe_info_json.json())["data"]["user_info"]["level_exps"][0]["level"]
        UID_LEVEL_ys = (MIYouShe_info_json.json())["data"]["user_info"]["level_exps"][1]["level"]
        UID_LEVEL_bh3 = (MIYouShe_info_json.json())["data"]["user_info"]["level_exps"][2]["level"]
        UID_LEVEL_bhxy = (MIYouShe_info_json.json())["data"]["user_info"]["level_exps"][3]["level"]
        UID_LEVEL_wdsjb = (MIYouShe_info_json.json())["data"]["user_info"]["level_exps"][4]["level"]
        UID_Create_time = (MIYouShe_info_json.json())["data"]["user_info"]["community_info"]["info_upd_time"]
        UID_Create_time = time.localtime(UID_Create_time)
        UID_Create_time = time.strftime("%Y{}%m{}%d{} %H{}:%M{}:%S{}", UID_Create_time).format("年", "月", "日", "时", "分",
                                                                                               "秒")
        UID_Watch = (MIYouShe_info_json.json())["data"]["user_info"]["achieve"]["follow_cnt"]
        user_normal = ("来了来了，客官您请求粉丝数量信息如下" +
                       "\n用户名：" + UID_name +
                       "\n个人简介:" + UID_introduce +
                       "\nUID：" + str(UID) +
                       "\n粉丝数：" + str(UID_follower) +
                       "\nTA关注的人数：" + str(UID_Watch) +
                       "\n获赞数：" + str(UID_like) +
                       "\n认证：" + UID_label) + \
                      "\n注册时间：" + UID_Create_time
        MIYouShe_LEVEL = "\n大别野等级：" + str(UID_LEVEL_dby) + \
                         "\n原神社区等级：" + str(UID_LEVEL_ys) + \
                         "\n崩坏学院社区等级：" + str(UID_LEVEL_bh3) + \
                         "\n崩坏3社区等级：" + str(UID_LEVEL_bhxy) + \
                         "\n未定事件薄社区等级：" + str(UID_LEVEL_wdsjb)
        return user_normal + MIYouShe_LEVEL

    def get_UID_MiYouShe_ys(self, UID):
        payload = {"uid": str(UID)}
        urls = "https://api-takumi.mihoyo.com/game_record/card/api/getGameRecordCard"
        MIYouShe_ys_json = requests.get(urls, params=payload, headers=self.get_Header())
        UID_name = (MIYouShe_ys_json.json())["data"]["list"][0]["game_role_id"]
        Ys_Game_ID = (MIYouShe_ys_json.json())["data"]["list"][0]["game_role_id"]
        YS_Game_Name = (MIYouShe_ys_json.json())["data"]["list"][0]["nickname"]
        Ys_Game_Region = (MIYouShe_ys_json.json())["data"]["list"][0]["region_name"]
        Ys_Game_Leve = (MIYouShe_ys_json.json())["data"]["list"][0]["level"]
        Ys_Game_Day = (MIYouShe_ys_json.json())["data"]["list"][0]["data"][0]["value"]
        Ys_Game_role_num = (MIYouShe_ys_json.json())["data"]["list"][0]["data"][1]["value"]
        Ys_Game_achi_num = (MIYouShe_ys_json.json())["data"]["list"][0]["data"][2]["value"]
        Ys_Game_tower_num = (MIYouShe_ys_json.json())["data"]["list"][0]["data"][3]["value"]
        _result = "\n游戏内ID：" + str(Ys_Game_ID) + "\n游戏内名称：" + YS_Game_Name + "\n服务器：" + Ys_Game_Region + \
                  "\n等级：" + str(Ys_Game_Leve) + "\n活跃天数：" + str(Ys_Game_Day) + "\n拥有角色数量" + \
                  str(Ys_Game_role_num) + "\n完成成就数：" + str(Ys_Game_achi_num) + "\n深境螺旋：" + str(Ys_Game_tower_num)
        _result = "----------*-----------\n" + "            原神玩家数据        " + _result
        return _result

    def get_UID_MiYouShe_bh3(self, UID):
        payload = {"uid": str(UID)}

        urls = "https://api-takumi.mihoyo.com/game_record/card/api/getGameRecordCard"
        MIYouShe_bh3_json = requests.get(urls, params=payload, headers=self.get_Header())

        bh3_Game_ID = (MIYouShe_bh3_json.json())["data"]["list"][1]["game_role_id"]
        bh3_Game_Name = (MIYouShe_bh3_json.json())["data"]["list"][1]["nickname"]
        bh3_Game_Region = (MIYouShe_bh3_json.json())["data"]["list"][1]["region_name"]
        bh3_Game_Leve = (MIYouShe_bh3_json.json())["data"]["list"][1]["level"]
        bh3_Game_Day = (MIYouShe_bh3_json.json())["data"]["list"][1]["data"][0]["value"]
        bh3_Game_role_num = (MIYouShe_bh3_json.json())["data"]["list"][1]["data"][1]["value"]
        bh3_Game_achi_num = (MIYouShe_bh3_json.json())["data"]["list"][1]["data"][2]["value"]
        bh3_Game_tower_num = (MIYouShe_bh3_json.json())["data"]["list"][1]["data"][3]["value"]
        _result = "\n游戏内ID：" + str(bh3_Game_ID) + "\n游戏内名称：" + bh3_Game_Name + "\n服务器：" + bh3_Game_Region + \
                  "\n等级：" + str(bh3_Game_Leve) + "\n累计登舰：" + str(bh3_Game_Day) + "\n圣痕数：" + \
                  str(bh3_Game_role_num) + "\n装甲数：" + str(bh3_Game_achi_num) + "\n服装数：" + str(bh3_Game_tower_num)
        _result = "----------*-----------\n" + "            崩坏3玩家数据        " + _result
        return _result
