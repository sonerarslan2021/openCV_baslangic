import cv2
import numpy as np

image1_path = "../cv2_baslangic/assets/globalaihub.png"

image1 = cv2.imread(image1_path)

kernel = np.ones((10, 10), np.uint8)

dilated_image = cv2.dilate(image1, kernel, iterations=1)

concatenated_image = np.concatenate((image1, dilated_image), axis=1)


concatenated_image= cv2.putText(concatenated_image, "Original Image:", (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (100, 100, 100), 1, cv2.LINE_AA, False)


cv2.imshow("Final Image", concatenated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()