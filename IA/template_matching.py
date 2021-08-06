#Programa Python Ejemplo
#Template Matching
import cv2
import numpy as np
#Leer la imagen principal
img_rgb = cv2.imread("total.png")
eye = cv2.imread("imagen.png")
#Convertir a escala gris
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
eye_gray = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(img_gray, eye_gray,cv2.TM_SQDIFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
print(min_val,max_val,min_loc,max_loc)

x1,y1 = min_loc
x2,y2 = min_loc[0] + eye.shape[1],min_loc[1] + eye.shape[0]



cv2.rectangle(img_rgb,(x1,y1),(x2,y2),(0,255,0),3)
cv2.imshow("img_rgb",img_rgb)
cv2.imshow("eye",eye)
cv2.waitKey(0)
