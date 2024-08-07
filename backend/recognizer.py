# Use a pipeline as a high-level helper
from transformers import pipeline
import os

model_name = "RavenOnur/Sign-Language"
pipe = pipeline("image-classification", model=model_name)

def use_pipe(image):
    prediction = pipe(image)
    most_probable = prediction[0]['label']
    return most_probable

if __name__ == "__main__":
    print('This is a test')
    imgdir = os.path.join('..', 'static', 'Images')
    imgpaths = [os.path.join(imgdir, img) for img in os.listdir(imgdir)]
    
    for imgpath in imgpaths:
        result = use_pipe(imgpath)
        print(imgpath, result)
        