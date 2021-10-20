import pandas as pd
import math

url = "http://tool.yurikago.net/644/yurikago/2012shokyakuritsu.html"
dfs = pd.read_html(url)

datas = dfs[1][["耐用年数（年）", "平成24年4月1日以後取得"]]

create_datas = "{"

for i in range(99):

    # 耐用年数
    year = i + 2

    create_datas += '"year' + str(year) + '": {'

    # 定額償却率 1を年数で割る なお、小数第四位を切り上げ
    up_num = 3  # 切り上げしたい桁
    target_num = 1 / year  # 切り上げ対象値
    teigaku_percent = math.ceil(target_num * 10 ** up_num) / (10 ** up_num)
    create_datas += '"teigaku"' + ': ' + str(teigaku_percent) + ","

    # 定率償却率 サイト引用
    create_datas += '"teiritsu"' + ': ' + str(datas["平成24年4月1日以後取得"]["定率法の償却率"][i]) + ","

    # 改定償却率 サイト引用
    if(str(datas["平成24年4月1日以後取得"]["改定償却率"][i]) == "―"):
        create_datas += '"kaitei"'   + ': ' + '"' + str(datas["平成24年4月1日以後取得"]["改定償却率"][i]) + '"' + ","
    else:
        create_datas += '"kaitei"'   + ': ' + str(datas["平成24年4月1日以後取得"]["改定償却率"][i]) + ","

    # 補償率 サイト引用
    if(str(datas["平成24年4月1日以後取得"]["保証率"][i]) == "―"):
        create_datas += '"hosho"'    + ': ' + '"' + str(datas["平成24年4月1日以後取得"]["保証率"][i]) + '"'
    else:
        create_datas += '"hosho"'    + ': ' + str(datas["平成24年4月1日以後取得"]["保証率"][i])


    #最後以外は,をつける
    if(i != 98):
        create_datas += "},"
    else:
        create_datas += "}"

create_datas += "}"

print(create_datas)
