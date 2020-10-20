import io, os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image
#exec(open('ss.py').read())
client = vision.ImageAnnotatorClient()

image_file = ImageGrab.grab((35, 95, 365, 365))
image_file.show()
imgByteArr = io.BytesIO()
image_file.save(imgByteArr, format='PNG')
imgByteArr = imgByteArr.getvalue()
content = imgByteArr

image = types.Image(content=content)

response = client.web_detection(image=image)
annotations = response.web_detection
            
for entity in annotations.web_entities:
    print(entity.description + '   ' + str(entity.score))
#hi
