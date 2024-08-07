# Use a pipeline as a high-level helper
from transformers import pipeline
import os

from transformers import ViTFeatureExtractor, ViTForImageClassification

model_name = "RavenOnur/Sign-Language"
pipe = pipeline("image-classification", model=model_name)

# feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
# model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
# pipe = pipeline("image-classification", model=model, feature_extractor=feature_extractor)
        
def use_pipe(image):
    #url = "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png"
    prediction = pipe(image)
    #prediction = pipe(url)
    most_probable = prediction[0]['label']
    return most_probable

if __name__ == "__main__":
    print('This is a test')
    imgdir = os.path.join('..', 'static', 'Images')
    imgpaths = [os.path.join(imgdir, img) for img in os.listdir(imgdir)]
    
    for imgpath in imgpaths:
        result = use_pipe(imgpath)
        print(imgpath, result)
        