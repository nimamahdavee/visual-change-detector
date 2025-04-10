import cv2
import numpy as np

def compare_images(image1_path, image2_path, output_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)

    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("No differences found.")
        cv2.imwrite(output_path, image2)
        return

    for contour in contours:
        if cv2.contourArea(contour) > 10:
            x, y, w, h = cv2.boundingRect(contour)
            padding = 8
            x = max(0, x - padding)
            y = max(0, y - padding)
            w += 2 * padding
            h += 2 * padding
            cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imwrite(output_path, image2)
    print(f"Output saved to {output_path}")



image1_path = "img1.png"
image2_path = "img2.png"


# image1_path = "image1_sample.png"
# image2_path = "image2_sample.png"
output_path = "output_sample.jpg"

compare_images(image1_path, image2_path, output_path)
