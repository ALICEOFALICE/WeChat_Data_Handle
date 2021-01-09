import werobot

from MiYouShe import *
from video_info import *

robot = werobot.WeRoBot(token='123456789')
test = get_MiYouShe()


@robot.text
def echo(message):
    User = message.content
    MiYouShe = get_MiYouShe()

    if re.match('bh3', User):
        UID = message.content
        UID = re.sub("bh3", "", UID)
        tag = MiYouShe.get_UID_MiYouShe_bh3(UID)
    elif re.match('ys', User):
        UID = message.content
        UID = re.sub("ys", "", UID)
        tag = MiYouShe.get_UID_MiYouShe_ys(UID)
    elif re.match('mys', User):
        UID = message.content
        UID = re.sub("mys", "", UID)
        tag = MiYouShe.get_UID_MiYouShe_info(UID)
    elif re.match('BV', User):
        UID = message.content
        tag = bilibili_info().get_video_info(UID)
    elif re.match('官服|B服', User):
        UID = message.content
        if re.match('官服', UID):
            SV="官服"
        else:SV="B服"
        UID=re.sub("官服|B服","",UID)
        print(UID)
        tag = MiYouShe.get_UID_MiYouShe_more(UID,SV)
    else:
        tag = ("----------*-----------\n" + (" "*4)+"桜火查询助手" +(" "*4) + "\n原神查询------ys+米游社UID"+ \
            "\n崩坏3查询 ---bh3 + 米游社UID" + "\n米游社查询---mys+米游社UID"+"\nB站视频查询---BV号")
    return tag


robot.run()
