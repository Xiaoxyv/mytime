import time

# time.struct_time(tm_year=2023, tm_mon=9, tm_mday=25, tm_hour=18, tm_min=10, tm_sec=27, tm_wday=0, tm_yday=268, tm_isdst=0)
#                   四位数年        月       日           时           分     秒         星期几0-6  一年的第几天    夏令时0，1，-1不确定
def get_now():
    week = ["一","二","三","四","五","六","日"]
    a = time.localtime()
    timedic = {"year":a[0],
                "month":a[1],
                "day":a[2],
                "hour":a[3],
                "min":a[4],
                "sec":a[5],
                "wday":week[a[6]],
                "yday":a[7],
                "dst":a[8]
                }
    return timedic

def str_timedic(timedic, mode="all"):
    try:
        Y = timedic["year"]
        y = str(Y)[-2:]
        m = timedic["month"]
        d = timedic["day"]
        H = timedic["hour"]
        h = (H-12) if H > 12 else H
        N = "下午" if H > 12 else "上午"
        Nen = "AM" if H > 12 else "PM"
        M = timedic["min"]
        S = timedic["sec"]
        wd = "星期"+timedic["wday"]
        yd = timedic["yday"]
        fyd = "365" if Y%4 else "366"
        if timedic["dst"]+1:
            dst = "夏令时" if timedic["dst"] else "非夏令时"
        if mode == "long":
            s = f"{Y}年{m}月{d}日 {H:0>2}:{M:0>2}:{S:0>2} {wd}"
            return s
        if mode == "all":
            s = f"{Y}年{m}月{d}日 {H:0>2}:{M:0>2}:{S:0>2} {wd} 第{yd}天 {dst}"
            return s
        if mode == "help":
            return "输入一请使用get_now获取时间字典，输入二为字符串：Y为四位年份，y为二位年份，m为月份，d为日期，H为24小时制，h为12小时制，N为上/下午，Nen对应为AM和PM，M为分钟，S为秒，wd为星期几，yd为一年的第几天，fyd可显示闰年366天，dst为夏令时状态。输入例子：\"#Y#年#m#月#d#日\"。已有预设模式\"long\"\"all\"可供使用。"
        newdic = {"Y":str(Y),"y":y,"m":str(m),"d":str(d),"H":f"{H:0>2}","h":f"{h:0>2}","M":f"{M:0>2}","S":f"{S:0>2}","wd":wd,"yd":str(yd),"dst":dst,"N":N,"Nen":Nen,"fyd":fyd}
        ls = mode.split("#")
        s = ""
        for i in ls:
            if i in newdic:
                s += newdic[i]
            else:
                s += i
        return s
    except:
        print("非法输入，请使用get_now获取时间字典")

if __name__ == "__main__" :
    a = get_now()
    print(str_timedic(a,"long"))
    print(str_timedic(a))
    # print(str_timedic(a,"help"))
    print(str_timedic(a,"#wd# 第#yd#/#fyd#天 当前时间：#h#:#M#:#S# #Nen# 日期：#Y#/#m#/#d#"))
    # 闰年测试
    a["year"] = 2024
    print(str_timedic(a,"#wd# 第#yd#/#fyd#天 -测试闰年2024- 日期：#Y#/#m#/#d#"))