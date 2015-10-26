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
    for index,value in enumerate(tmp_list.keys()):
        print index,value
    print index+1,"back to up layer"
    print index+2,"quit"

    #check the validity of input
    services_choose = raw_input()
    if services_choose.isdigit():
        services_choose = int(services_choose)
        if services_choose >= len(tmp_list)+2:
            print("choose error,please retry")
            continue
    else:
        print("choose error,please retry")
        continue

    if services_choose == len(tmp_list):
        if level == 0:
            print("top level,cannot back to up")
            continue
        else:
            level -= 1
            tmp_list = up_list
            continue
    if services_choose == len(tmp_list)+1:
        break
    key = tmp_list.keys()[services_choose]
    if key in tmp_list.keys():
        up_list = tmp_list
        tmp_list = tmp_list[key]
        if level == 2:
            print(tmp_list)
            break
        level += 1
    else:
        print("choose error")


