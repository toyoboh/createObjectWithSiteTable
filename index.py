import pandas as pd

url = "http://tool.yurikago.net/644/yurikago/2012shokyakuritsu.html"
dfs = pd.read_html(url)

datas = dfs[1][["耐用年数（年）", "平成24年4月1日以後取得"]]

create_datas = "{"

for i in range(99):
    create_datas += '"year' + str(i + 2) + '": {'
    create_datas += '"teiritsu"' + ': ' + str(datas["平成24年4月1日以後取得"]["定率法の償却率"][i]) + ","

    if(str(datas["平成24年4月1日以後取得"]["改定償却率"][i]) == "―"):
        create_datas += '"kaitei"'   + ': ' + '"' + str(datas["平成24年4月1日以後取得"]["改定償却率"][i]) + '"' + ","
    else:
        create_datas += '"kaitei"'   + ': ' + str(datas["平成24年4月1日以後取得"]["改定償却率"][i]) + ","

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
