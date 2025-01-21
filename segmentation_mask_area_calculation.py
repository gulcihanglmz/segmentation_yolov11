import cv2
import numpy as np
import os

# Doluluk oranını hesaplayan fonksiyon
def calculate_fill_ratio(mask, correction_percentage= 2.5):
    # Görüntü boyutlarını al
    height, width = mask.shape[:2]

    # Çevreden kırpma miktarını hesapla
    crop_h = int(height * correction_percentage / 100)  # Yükseklikten kırpma miktarı
    crop_w = int(width * correction_percentage / 100)   # Genişlikten kırpma miktarı

    # kırp (üst, alt, sol, sağ kenarları küçült)
    remaining_area = mask[crop_h:height - crop_h, crop_w:width - crop_w]

    # İçerdeki beyaz (maskelenmiş) alanın toplamını say
    masked_area = np.sum(remaining_area > 0)  # Beyaz piksel sayısı

    # Kalan alanın toplam alanını hesapla (örn: pixel sayısı)
    remaining_area_size = remaining_area.size

    # Doluluk oranını hesapla
    fill_ratio = (masked_area / remaining_area_size) * 100

    return fill_ratio

# Girdi ve çıktı klasörlerini tanımlayın
input_folder = r"D:\segmentation\images"  # Orijinal görüntülerin bulunduğu klasör
mask_folder = r"D:\segmentation\results-yolov11s_e50_i256"  # Maskelerin bulunduğu klasör
output_folder = r"D:\segmentation\results_with_percentage"  # Sonuçların kaydedileceği klasör

# Çıktı klasörünü oluştur
os.makedirs(output_folder, exist_ok=True)

# Görseller üzerinde işlem yap
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        # Görüntü ve maske dosya yollarını tanımlayın
        image_path = os.path.join(input_folder, file_name)
        mask_path = os.path.join(mask_folder, file_name)

        # Görüntü ve maskeyi yükle
        image = cv2.imread(image_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)  # Maskeyi gri tonlamalı olarak yükle

        if image is not None and mask is not None:
            # Doluluk oranını hesapla (çevreden %0.5 kırpma)
            correction_percentage = 0.5  # Çevreden %0.5 kırpma
            fill_ratio = calculate_fill_ratio(mask, correction_percentage)

            # Görüntünün üzerine oranı yaz (kısa format ve küçük boyut)
            output_image = image.copy()
            text = f"Doluluk: {fill_ratio:.2f}%"  # Daha kısa format
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.8  # Daha küçük yazı boyutu
            font_thickness = 2
            text_color = (0, 255, 0)  # Yeşil renk
            cv2.putText(output_image, text, (20, 30), font, font_scale, text_color, font_thickness)

            # İşlenmiş görüntüyü kaydet
            output_path = os.path.join(output_folder, file_name)
            cv2.imwrite(output_path, output_image)
            print(f"{file_name} işlendi ve kaydedildi.")
        else:
            print(f"{file_name} yüklenemedi veya maske bulunamadı!")

print("Tüm görseller işlendi ve sonuçlar kaydedildi.")
