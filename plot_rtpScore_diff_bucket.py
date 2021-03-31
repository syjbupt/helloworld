# encoding=utf8
import sys,os
import pandas as pd
# read csv file
fname = "/Users/sunyijia/Documents/workResource/飞猪推荐/酒店业务/酒店推荐-排序模型线上实验_0325.xlsx"

df = pd.read_excel(fname, sheet_name=u"online_auc分析")

mindate = 20210324
maxdate = 20210329
exp_data = df[df["ds"] >= mindate]
exp_data = exp_data[exp_data["ds"] <= maxdate]
print(exp_data.head())

abid_group = exp_data.groupby(by = ["ab_id"])

import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
plt.style.use('seaborn')

for ylabel in ["ctr_auc", "ctr_gauc", "rtp_ctr_auc", "rtp_ctr_gauc"]:
    # 设置x轴
    plt.figure(figsize=(9, 6))
    # 配置横坐标
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m.%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    for groupname, gdata in abid_group:
        if groupname == "5448_26167":
            continue
        dates = [str(d) for d in abid_group.get_group(groupname)["ds"]]
        xs = [datetime.strptime(d, '%Y%m%d').date() for d in dates]
        y2 = abid_group.get_group(groupname)[ylabel]
        if groupname == "5448_25331":
            groupname = "exp"
        plt.plot(xs, y2, "-o", label = groupname)
    plt.xlabel("dates")
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(ylabel)
    plt.gcf().autofmt_xdate()
    plt.show()
