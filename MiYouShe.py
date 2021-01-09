import random
import string
import time
import hashlib
import requests


class get_MiYouShe:
    def __init__(self):
        self.cookie = ""
        self.headers = {"user_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Geck\
        o) Chrome/81.0.4044.113 Safari/537.36"}

    def hexdigest(self, text):
        md5 = self.md5()
        md5.update(text.encode())
        return md5.hexdigest()

    def md5(self, text):
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()
    def getDS(self):
        n = 'h8w582wxwgqvahcdkpvdhbh2w9casgfl'
        i = str(int(time.time()))
        r = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
        c = get_MiYouShe().md5("salt=" + n + "&t=" + i + "&r=" + r)
        print("{},{},{}".format(i, r, c))
        return "{},{},{}".format(i, r, c)

    def get_Header(self):
        headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN",
            "x-rpc-client_type":"5",
            "DS":(self.getDS()),
            "x-rpc-app_version":"2.3.0",
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.3.0 Edg/88.0.4324.50",
            "Origin":"https://webstatic.mihoyo.com",
            "Referer":"https://webstatic.mihoyo.com/",
            "Cookie":"UM_distinctid=17640c883e881e-0b0158e275dc8b-5a301d45-1fa400-17640c883e9b52; _MHYUUID=b8d0a43f-11f8-4fc1-a08c-2f3fa16d373a; _gid=GA1.2.811078272.1610010362; account_id=20934997; cookie_token=9s3s1IPuXFz3c1cLthZYpXmW8Hp38atkKHU0lJDd; ltoken=eYUYQm65nUHBpPaeopzwJrksdE0KCopDGxoRmUs0; ltuid=20934997; _ga_KJ6J9V9VZQ=GS1.1.1610016172.3.1.1610017600.0; _ga=GA1.2.561767950.1607404652"
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
        urls = "https://api-takumi.mihoyo.com/game_record/card/wapi/getGameRecordCard?"
        MIYouShe_ys_json = requests.get(urls, params=payload,headers=self.get_Header())
        print(MIYouShe_ys_json)
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
                  "\n等级：" + str(Ys_Game_Leve) + "\n活跃天数：" + str(Ys_Game_Day) + "\n拥有角色数量：" + \
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

    def get_UID_MiYouShe_more(self,UID,SV):
        _result=""
        if SV == "官服":
            server="cn_gf01"
        else: server="cn_gf02"
        payload = {"server":server,"role_id": str(UID)}
        urls = "https://api-takumi.mihoyo.com/game_record/genshin/api/index?"
        MIYouShe_ys_json = requests.get(urls, params=payload,headers=self.get_Header())
        _MiYouShe_ys_Role_Path=(MIYouShe_ys_json.json())["data"]["avatars"]
        _MiYouShe_ys_Role_Path_2 = (MIYouShe_ys_json.json())["data"]["world_explorations"]
        for _MiYouShe_ys_Role_Path_open in _MiYouShe_ys_Role_Path:
            _result_air=""
            _result_air = "\n角色名：" + str(_MiYouShe_ys_Role_Path_open["name"]) + "\n等级：" + \
                      str(_MiYouShe_ys_Role_Path_open["fetter"]) + "\n好感度：" + str(_MiYouShe_ys_Role_Path_open["level"])
            _result=_result+_result_air
        _result=_result+"\n---------------"
        for _MiYouShe_ys_Role_Path_open in _MiYouShe_ys_Role_Path_2:
            _result_air="\n"+_MiYouShe_ys_Role_Path_open["name"]+"等级:"+str(_MiYouShe_ys_Role_Path_open["level"])
            _result=_result+_result_air
        _result = "----------*-----------\n" + "            原神角色数据        " + _result
        return _result





