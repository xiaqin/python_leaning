__author__ = 'xiaqin'

city = {
    "school": {
        "jiaotong": {
            "compute sc": ["xiaofeng", "zhihong", "zhier"],
            "Art": ["xiaolin", "xuebin", "weigang"],
            "physics": ["wenlan", "wenhan", "xiaobin"]
        },
        "fudan": {
            "press": ["fujin", "xiangping", "xiaomin"],
            "compute sc": ["aa", "bb", "cc"],
            "chmistry": ["dd", "ee", "ff"]
        }
    },
    "company": {
        "cisco": {
            "ipcbu": ["xiaofeng_cisco", "zhihong_cisco", "zhier_cisco"],
            "tipbu": ["xiaolin_cisco", "xuebin_cisco", "weigang_cisco"],
            "cdbu": ["wenlan_cisco", "wenhan_cisco", "xiaobin_cisco"]
        },
        "alcatel": {
            "dd_bu": ["fujin_al", "xiangping_al", "xiaomin_al"],
            "ff_bu": ["aa_al", "bb_al", "cc_al"],
            "tt_bu_": ["dd_al", "ee_al", "ff_al"]
        }
    }
}

tmp_list = city.copy()

level = 0

while True:
    print("please choose the following services")
    print(tmp_list.keys())
    services_choose = raw_input()
    if services_choose in tmp_list.keys():
        tmp_list = tmp_list[services_choose]
        if level == 2:
            print(tmp_list)
            break
        level += 1
    else:
        print("choose error")


