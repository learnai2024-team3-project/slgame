import cv2
import torch
from ultralytics import YOLO

# If a GPU (CUDA) is available, use it;
# otherwise, fall back to using the CPU.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Using device: {device}')

# Load the model and move it to the device
model = YOLO('./models/best.pt')
model.to(device)


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
        return (model.names[int(label)], conf)

    return ("", 0.0)
