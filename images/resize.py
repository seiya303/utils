import cv2
IMGNAME = "sign.jpg"
img = cv2.imread(IMGNAME, cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
 
print('Resized Dimensions : ',resized.shape)
# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)

cv2.imwrite("resized_"+IMGNAME, resized)

cv2.destroyAllWindows()
 