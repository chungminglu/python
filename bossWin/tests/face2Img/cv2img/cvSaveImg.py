import cv2
img=cv2.imread("./gg.jpg")
cv2.imshow("sss",img)
k=cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("./tt.jpg",img)
    cv2.destroyAllWindows()
