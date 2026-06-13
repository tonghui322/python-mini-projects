import os
import shutil
import sys
import cv2

class FrameCapture:
    def __init__(self, file_path):
        self.directory = "captured_i_frames"  # 文件夹改名区分I帧
        self.file_path = file_path
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_i_frames_only(self):
        cap = cv2.VideoCapture(self.file_path)
        if not cap.isOpened():
            print("视频打开失败，请检查路径")
            return

        save_idx = 0
        frame_idx = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 判断当前帧是否为I帧
            frame_type = cap.get(cv2.CAP_PROP_FRAME_TYPE)
            # 7 代表 I帧；6=P帧，8=B帧
            if frame_type == 7:
                save_path = f'{self.directory}/i_frame_{save_idx}.jpg'
                cv2.imwrite(save_path, frame)
                print(f"已保存I帧：i_frame_{save_idx}.jpg  原帧序号：{frame_idx}")
                save_idx += 1

            frame_idx += 1

        cap.release()
        print(f"\n提取完成，一共找到 {save_idx} 个I帧")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python capture_video_frames.py 视频完整路径")
        sys.exit(0)
    file_path = sys.argv[1]
    fc = FrameCapture(file_path)
    fc.capture_i_frames_only()