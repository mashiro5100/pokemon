import requests
from bs4 import BeautifulSoup

res = requests.get(
    "https://wiki.52poke.com/zh-hans/%E5%B1%9E%E6%80%A7%E7%9B%B8%E5%85%8B%E8%A1%A8"
)
# print(res.text)

bs = BeautifulSoup(res.text, "lxml")
tb = bs.find(
    "table",
    style="border: 2px solid #111; background:#808080; margin-right: 5px; margin-bottom: 5px;",
)
rows = list(tb.find("tbody").children)


titles = [
    "一般",
    "格斗",
    "飞行",
    "毒",
    "地面",
    "岩石",
    "虫",
    "幽灵",
    "钢",
    "火",
    "水",
    "草",
    "电",
    "超能力",
    "冰",
    "龙",
    "恶",
    "妖精",
]


rv = []
for tr in rows[3:-1]:
    #
    a = tr.find("a")
    if type(a) is int:
        continue
    attr = a.string
    print(attr)
    # print(tr)
    temp = []
    for td in tr.find_all("td"):
        # s = str(td.string)
        # # print(type(s))
        # if type(s) is str:
        #
        #     s = s.strip()
        #     if s.endswith('×'):
        #         temp.append(int(s[0]))
        sup = td.find("sup")
        sub = td.find("sub")
        if sup and sub:
            temp.append(int(sup.string) / int(sub.string))
        else:
            s = str(td.string)
            s = s.strip()
            if s.endswith("×"):
                temp.append(int(s[0]))
    rv.append(temp)

print(rv)
m = [
    [1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],
    [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
    [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
    [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
    [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
    [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
    [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],
    [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
    [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
    [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
    [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
    [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1],
]
