import cv2
import torch
from ultralytics import YOLO
import tempfile

# 检查并使用GPU或CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Using device: {device}')

# 加载模型并将其移动到设备
model = YOLO('./models/best.pt')
model.to(device)

def recognize_video(file_byte):
    # 创建一个临时文件来存储视频
    with tempfile.NamedTemporaryFile(suffix='.webm') as temp_video_file:
        # 将字节流写入临时文件
        temp_video_file.write(file_byte)
        temp_video_file.flush()

        # 打开视频文件
        video_capture = cv2.VideoCapture(temp_video_file.name)
        
        highest_conf = 0
        best_label = ""

        # 检查视频是否成功打开
        if not video_capture.isOpened():
            print("无法打开视频文件")
            return best_label, highest_conf
        
        # 逐帧处理视频
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # 调用 recognize_image 识别每一帧
            label, conf = recognize_image(frame)
            
            # 更新最高置信度的结果
            if conf > highest_conf:
                highest_conf = conf
                best_label = label

        # 释放视频捕获对象
        video_capture.release()

    return best_label, highest_conf
    
    
def recognize_image(image):
    # 找到最高置信度的检测结果
    best_result = None
    max_conf = 0
    
    # 设置置信度阈值
    confidence_threshold = 0.25
    
    results = model(image, conf=confidence_threshold)

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()  # 获取边界框
        confs = result.boxes.conf.cpu().numpy()  # 获取置信度
        labels = result.boxes.cls.cpu().numpy()  # 获取分类标签
        
        for box, conf, label in zip(boxes, confs, labels):
            if conf > max_conf:
                max_conf = conf
                best_result = (box, conf, label)

    # 绘制最高置信度的检测结果
    if best_result is not None:
        box, conf, label = best_result
        return (model.names[int(label)], conf)
    
    return ("", 0.0)
