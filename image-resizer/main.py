import cv2



scale_percent=int(input("Enter the proportion of img that you want"))

img = cv2.imread("download.jpeg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("Original Image", img)

# Resizing the image

width = int(img.shape[1] * scale_percent )
height = int(img.shape[0] * scale_percent)
dim = (width, height)
resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized Image", resized_img)

# Saving the resized image with a different filename
output_filename = "resized_image.png"
cv2.imwrite(output_filename, resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
