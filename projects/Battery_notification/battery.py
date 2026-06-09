import psutil
from plyer import notification

#step1 获取设备当前电量
def get_battery():
    battery = psutil.sensors_battery()
    if battery:
        #剩余电量百分比
        percent =  battery.percent
        #是否正在充电 True充电/False未充电
        is_plugged = battery.power_plugged
        #剩余秒数
        secs_left = battery.secsleft

        print(f"当前电量：{percent}%")
        print(f"电源适配器连接：{is_plugged}")
        print(f"剩余可用时长：{secs_left}秒")

        return percent, is_plugged
    else:
        print("当前设备无电池（台式机）")
        return None, None

#step2 做系统通知
def push_battery(percent, is_plugged):
    plugged = ""
    if is_plugged:
        plugged = "正在充电"
    else:
        plugged = "未充电"
    
    msg = f"电池电量为：{percent}%,充电状态：{plugged}"
    #三方依赖库 推送系统通知
    notification.notify(
        title="电池状态提醒",
        message=msg,
        timeout=5
    )
    print("通知完成")
    return

if __name__ == "__main__":
    battery_num, plugged_status = get_battery()
    push_battery(battery_num, plugged_status)
    print("程序执行完成")