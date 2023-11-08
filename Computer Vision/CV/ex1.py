import cv2 #library Import

img = cv2.imread("sample2.jpg") #read an image

cv2.imwrite("sample1Copy.png",img) #save an image

cv2.imshow("AI_Master_Class",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
