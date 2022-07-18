#JSON FILEGA YOZISH

# from data import maxsulotlar
# import json

# jsondata = json.dumps(maxsulotlar,indent=4)

# file = open("data.json","w")

# file.write(jsondata)

# file.close()

#JSON FILEDAN OLISH


# import json

# file = open("data.json","r")

# data = json.loads(file.read())

# print(data)
"""
print(
    list(
        filter(
            lambda x:(not x.startswith("__")),
            dir(data)
            )
        )
    )

"""
import data
import json

with open("maxsulotlar.json","w") as maxsulotlar_json:
    maxsulotlar_data = json.dumps(
        data.maxsulotlar,
        indent=4
        )
    maxsulotlar_json.write(maxsulotlar_data)

with open("xaridorlar.json","w") as xaridorlar_json:
    xaridorlar_data = json.dumps(
        data.xaridorlar,
        indent=4,
        )
    xaridorlar_json.write(
        xaridorlar_data
        )

with open("admins.json","w") as admins_json:
    admins_data = json.dumps(
        data.DOKON_EGALARI,
        indent=4,
        )
    admins_json.write(
        admins_data
        )
m_mal = open("maxsulotlar_malumoti.json","w")
m_mal_data = json.dumps(
    data.maxsulotlar_malumoti,
    indent=4,
    )
print(m_mal_data, file=m_mal)
m_mal.close()



















