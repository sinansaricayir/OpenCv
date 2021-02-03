# 1. Kullanacağımız kütüphane çalışmamıza dahil edilir.
import cv2   


# 2. Kullanacağımız resim çalışmamıza dahil edilir.
img = cv2.imread("C:\\Users\\Sinan\\Desktop\\opencv-final\\photos\\sinan3.jpg")

# 3. Kullanacağımız cascade dosyası çalışmamıza dahil edilir.
face_cascade = cv2.CascadeClassifier("C:\\Users\\Sinan\\Desktop\\opencv-final\\frontalface.xml")

# 4. Haar-like özellikleri kolay algılayabilmek için resmimizi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 5. Şimdi de cascade dosyamızı kullanarak resim üzerindeki yüzlerin koordinarlarını bulalım.
faces = face_cascade.detectMultiScale(gray, 1.3, 7)

# 6. "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# 7. İşlediğimiz resmi görelim.
cv2.imshow('Sinan Saricayir - Final Projesi ',img)

# 8. Son olarak programı kapatacak kodu yazalım.
cv2.waitKey(0)
cv2.destroyAllWindows()
