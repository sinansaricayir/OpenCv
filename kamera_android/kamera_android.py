import cv2
import numpy as np
import requests

url ="http://192.168.1.104:8080//shot.jpg"
#url değişkeni oluşturularak içerisine android kameradan alınan adres yazılır

while True:
    img_resp = requests.get(url) #requests kütüphanesinin fonksiyonu kullanılarak görüntü adresi kullanılır
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    #Alınan görüntü bir array içerisinde tutulur ve bytearray'e çevirilir
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR) #Hafızadan çekilen görüntüyü görüntülenebilir hale getirir
    img = cv2.resize(img,(640,480)) # Görüntü boyutlandırılır

    cv2.imshow("Android Kamera",img) # Resimin görüntüleneceği pencere

    if cv2.waitKey(1)==27:
        break


cv2.destroyWindow()