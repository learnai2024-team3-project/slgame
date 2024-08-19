import cv2
import torch
from ultralytics import YOLO
import tempfile

# If a GPU (CUDA) is available, use it;
# otherwise, fall back to using the CPU.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Using device: {device}')

# Load the model and move it to the device
model = YOLO('./models/best.pt')
model.to(device)

def recognize_video(file_byte):
    # 创建一个临时文件来存储视频
    with tempfile.NamedTemporaryFile(suffix='.webm', mode='wb+', delete=False) as temp_video_file:
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
            label, conf, _ = recognize_image(frame)
            
            # 更新最高置信度的结果
            if conf > highest_conf:
                highest_conf = conf
                best_label = label

        # 释放视频捕获对象
        video_capture.release()

    return best_label, highest_conf

def recognize_image(image):
    # Find the detection result with the highest confidence
    best_result = None
    max_conf = 0

    # Set the confidence threshold
    confidence_threshold = 0.25

    results = model(image, conf=confidence_threshold)

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()  # Get bounding boxes
        confs = result.boxes.conf.cpu().numpy()  # Get confidences
        labels = result.boxes.cls.cpu().numpy()  # Get class labels

        for box, conf, label in zip(boxes, confs, labels):
            if conf > max_conf:
                max_conf = conf
                best_result = (box, conf, label)

    # Draw the detection result with the highest confidence
    if best_result is not None:
        box, conf, label = best_result
        x1, y1, x2, y2 = map(int, box)
        label_text = f'{model.names[int(label)]} {conf:.2f}'
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        return (model.names[int(label)], conf)

    return ("", 0.0)
