 # 中文时间串 mytime
 ## 简介 Introduce
 简易的自定义时间格式函数，可自定义输入。
 ## 使用方式 Usage
 自定义模式时使用 #h# 等作为格式化参数
```py
from mytime import *
timedic = get_now()
# 输出预设完整时间串
timestr = str_timedic(timedic)
print(timestr)
# 输出预设长时间串
timestr = str_timedic(timedic,"long")
print(timestr)
# 自定义时间串
timestr = str_timedic(timedic,\
    "当前时间：#h#:#M#:#S#\
     日期：#Y#/#m#/#d#")
print(timestr)
# 查看参数帮助
timestr = str_timedic(timedic,"help")
```
 ## 参数列表 Parameter
 Y为四位年份，y为二位年份，m为月份，d为日期，H为24小时制，h为12小时制，N为上/下午，Nen对应为AM和PM，M为分钟，S为秒，wd为星期几，yd为一年的第几天，fyd可显示闰年366天，dst为夏令时状态
|参数|描述|
|:---:|:---:|
|#Y#|四位年份（如：2023）|
|#y#|二位年份（如：23）|
|#m#|月份|
|#d#|日期|
|#H#|24小时制时数|
|#h#|12小时制时数|
|#N#|显示中文“上午”，“下午”|
|#Nen#|显示英文“PM”，“AM”|
|#M#|分数|
|#S#|秒数|
|#wd#|星期几|
|#yd#|显示一年的第几天|
|#fyd#|闰年则为366天，其他为365天|
|#dst#|夏令时状态：“夏令时”，“非夏令时”|

**查看自带用例**
```
python mytime.py
```
本项目遵循MIT开源协议
