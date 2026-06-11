#定时任务 截屏
import time
import os
from mss import MSS
from mss.tools import to_png

#截屏
def gen_screenshot(save_path="./"):
    # 自动创建存储文件夹
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 捕获主屏幕
    with MSS() as screen_capture:
        monitor = screen_capture.monitors[1]
        capture_img = screen_capture.grab(monitor)
        # 时间戳命名
        file_name = f"screen_{int(time.time())}.png"
        full_save_path = os.path.join(save_path, file_name)
        # 标准转换保存
        to_png(capture_img.rgb, capture_img.size, output=full_save_path)
        print(f"截图已保存：{full_save_path}")

if __name__ == "__main__":
    # 每20秒截取一次
    while True:
        gen_screenshot()
        time.sleep(20)