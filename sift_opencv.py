import cv2

img = cv2.imread("gandalf.jpg")

sift = cv2.xfeatures2d.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, keypoints, None)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
