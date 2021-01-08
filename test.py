c = input("123")
import re

if re.match('bh3', c):
    print("崩三")
elif re.match('ys', c):
    print("原神")
elif re.match('mys', c):
    print(re.sub("mys", "123", c))
else:
    "没有匹配"
