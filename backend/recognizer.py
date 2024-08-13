import cv2
import torch
from ultralytics import YOLO

# 检查并使用GPU或CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Using device: {device}')

# 加载模型并将其移动到设备
model = YOLO('./models/best.pt')
model.to(device)

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
