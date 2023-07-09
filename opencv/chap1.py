import cv2

img=cv2.imread("i.jpg")
print(img.shape)

# cv2.imshow("Image",img)
imgresize=cv2.resize(img,(600,300))

imgcrop=img[0:200,200:500]

cv2.imshow("Image",imgresize)
cv2.imshow("Imagecrop",imgcrop)

cv2.waitKey(0)
