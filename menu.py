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

while True:
    print("please choose the following services")
    print(city.keys())
    services_top = raw_input()
    if services_top in city.keys():
        print("now you choose %s list" %services_top)
        service_list = city[services_top]
        print("there are following items to choose:")
        print(service_list.keys())
        service_2 = raw_input()
        print("now you choose %s " %service_2)
    else:
        print("choose error")
    break

