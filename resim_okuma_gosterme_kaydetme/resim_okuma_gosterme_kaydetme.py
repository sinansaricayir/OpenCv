import cv2  #Projeye OpenCV kütüphanesi eklenir

img = cv2.imread("gunbatimi.jpg")
#img değişkeni oluşturulur
#Ve cv2.imread fonksiyonu ile projede kullanılacak resimlerin matematiksel değerleri okunur
#Fonksiyon içerisine işlenecek olan resim yolu yazılır
#Resim ve .py aynı klasörde olduğu için resim adı.uzatısı yazılabilir

cv2.namedWindow("image",cv2.WINDOW_NORMAL)


cv2.imshow("image",img)
#İçerisine iki adet argüman alır, ilki resmin göstereleceği pencerenin adı
#ikincisi ise resmimin tutulduğu değişken

cv2.imwrite("gunbatimi.jpg",img)


cv2.waitKey(0)
#Fonksiyon içerisine girilen değer (milisaniye) kadar ekranda tutulur

cv2.destroyAllWindows() # Tüm pencerelerin kapatılması için kullanılır