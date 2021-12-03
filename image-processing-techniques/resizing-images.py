import cv2

image = cv2.imread("../cv2_baslangic/assets/img.png")

scale_rate = 0.5
height = int(image.shape[0] * scale_rate)
width = int(image.shape[1] * scale_rate)
image_resized = cv2.resize(image, (width, height))

cv2.imshow("Resized Image", image_resized)
cv2.waitKey(0)
