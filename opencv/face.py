import  cv2


facescsd=cv2.CascadeClassifier("")
img=cv2.imread("images (1).jpeg")
cv2.imshow("result",img)
cv2.waitKey(0)