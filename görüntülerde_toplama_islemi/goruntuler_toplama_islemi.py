import cv2
import numpy as np


circle=np.zeros((512,512,3),np.uint8) + 255 #Beyaz renkte bir tuval oluşturur

cv2.circle(circle, (256,256), 60 , (255,0,0) , -1) #Oluşturulan beyaz tuvalin merkezine mavi renkte çember çizilir


circle2=np.zeros((512,512,3),np.uint8) + 255 #Tekrardan beyaz renkte bir tuval oluşturur

cv2.circle(circle2, (256,256), 60 , (0,0,255) , -1) #Oluşturulan beyaz tuvalin merkezine kırmızı renkte çember çizilir


add=cv2.add(circle,circle2) #add değişkeni oluşturularak çemberlerin değeri toplanır

print(add) #Consol ekranında oluşturulan toplama işleminin sayısal değerini görmek istediğim için ekledim




cv2.imshow("Circle",circle)
cv2.imshow("Circle2",circle2)
cv2.imshow("Toplam",add)


cv2.waitKey(0)
cv2.destroyAllWindows()