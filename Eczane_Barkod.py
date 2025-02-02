import cv2
from pyzbar.pyzbar import decode
import sys

def barkod_canli_goruntu():
    cap = cv2.VideoCapture(0)
    #print("Kamera başlatıldı. 'q' tuşuna basarak çıkabilirsiniz.")

    while True:
        ret, frame = cap.read()
        if not ret:
            #print("Kamera görüntüsü alınamadı.")
            break

        barkodlar = decode(frame)
        for barkod in barkodlar:
            barkod_verisi = barkod.data.decode("utf-8")  # Barkod verisini aldım.
            barkod_tipi = barkod.type

            # Barkodun bulunduğu dikdörtgeni çizdim.
            x, y, w, h = barkod.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Barkod bilgilerini ekrana yazdım.
            metin = f"{barkod_tipi}: {barkod_verisi}"
            cv2.putText(frame, metin, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            # Barkod bilgilerini C#'a göndermek için konsola yazdım.
            print(barkod_verisi)

            # Kamera görüntüsünü kapattım.
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()  # İlk barkodu algıladığında çıkış yaptım.

        # Görüntüyü ekranda gösterdim.
        cv2.imshow("Canlı Barkod Okuyucu", frame)

        # 'q' tuşuna basıldığında çıktım.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Canlı barkod okuma fonksiyonunu çalıştırdım.
barkod_canli_goruntu()
