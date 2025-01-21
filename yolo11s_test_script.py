import os
from ultralytics import YOLO
import cv2
import numpy as np

# Modeli yükle
model = YOLO(r"D:\segmentation\segmentasyon_8s_50e_256i.pt")

# Girdi ve çıktı klasörlerini tanımlayın
input_folder = r"D:\segmentation\Images test"  # Görsellerin olduğu klasör
output_folder = r"D:\segmentation\results_yolov11s_50e_i256"  # Maskelerin kaydedileceği klasör

# Tüm görselleri işleme döngüsü
for file_name in os.listdir(input_folder):
    # Sadece resim dosyalarını seç (örnek: jpg, png)
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        # Görüntünün tam yolunu oluştur
        image_path = os.path.join(input_folder, file_name)

        # Görüntüyü yükle
        image = cv2.imread(image_path)

        # Segmentasyon işlemi
        results = model(image, task="segment")

        # Segmentasyon maskesi oluştur ve kaydet
        if len(results[0].masks.data) > 0:  # Eğer mask varsa
            mask = results[0].masks.data[0].cpu().numpy()  # İlk maskeyi al
            mask_output_path = os.path.join(output_folder, file_name)  # Çıktı dosya yolu
            cv2.imwrite(mask_output_path, (mask * 255).astype("uint8"))  # Maskeyi kaydet

print("Tüm görseller işlendi ve maskeler kaydedildi.")

