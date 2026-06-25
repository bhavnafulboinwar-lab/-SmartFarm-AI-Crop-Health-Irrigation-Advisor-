import cv2
import numpy as np

def predict_disease(image_path):
    

    img = cv2.imread(image_path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    green_pixels = cv2.inRange(
        hsv,
        (35,40,40),
        (85,255,255)
    )

    green_ratio = np.sum(green_pixels > 0) / green_pixels.size

    if green_ratio > 0.6:
        return "Healthy Plant"
    elif green_ratio > 0.3:
        return "Leaf Spot Disease"
    else:
        return "Blight Disease"

def irrigation_advisor(
        soil,
        temp,
        humidity):

    if soil < 30:
        return "Water Immediately"

    elif soil < 50:
        return "Water within 12 Hours"

    else:
        return "No Irrigation Required"