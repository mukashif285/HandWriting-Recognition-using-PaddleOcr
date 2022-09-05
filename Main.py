

# # # GitHub repo installation of paddle
# !python -m pip install paddlepaddle-gpu==2.2.0 -i https://mirror.baidu.com/pypi/simple
# # !python3 -m pip install paddlepaddle-gpu== 2.3.1 -f https://paddlepaddle.org.cn/whl/stable/noavx.html

# !pip install paddlepaddle

# # Install paddle OCR
# !pip install paddleocr

# # Clone paddle OCR repo - get FONTS for visualization
# !git clone https://github.com/PaddlePaddle/PaddleOCR

from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation
import urllib.request
from PIL import Image

# Setup model
def Main(img_pathe):
    ocr_model = PaddleOCR(lang='en')

    #img_path = Image.open(img_path)
    img_path=urllib.request.urlretrieve(img_pathe, )
    #print (img_path)
    # Run the ocr method on the ocr model
    result = ocr_model.ocr("kungfupanda.jpg")
    x = []
    for res in result:
        x.append(res[1][0])

    # Extracting detected components
    boxes = [res[0] for res in result] 
    texts = [res[1][0] for res in result]
    scores = [res[1][1] for res in result]

    # Specifying font path for draw_ocr method
    font_path = os.path.join('PaddleOCR', 'doc', 'fonts', 'latin.ttf')

    # Import our image - drug 1/2/3
    # imports image
    img = cv2.imread("kungfupanda.jpg") 

    # reorders the color channels
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Visualize our image and detections
    # resizing display area
    plt.figure(figsize=(15,15))

    # draw annotations on image
    annotated = draw_ocr(img, boxes, texts, scores, font_path=font_path) 

    # show the image using matplotlib
    plt.imshow(annotated)

    
    # save image
    status = cv2.imwrite('output.jpg',annotated)
    
    print("Image written to file-system : ",status)

Main("https://raw.githubusercontent.com/mukashif285/Mustafa/master/dope.jpg")
