# Alzheimer MRI Sınıflandırma Projesi

Bu depo, Alzheimer hastalığının farklı evrelerini sınıflandırmak için TensorFlow ve Keras kullanılarak oluşturulmuş bir Konvolüsyonel Sinir Ağı (CNN) modelini içermektedir. Sınıflandırılan evreler şunlardır:

- **Yok (Alzheimer Yok)**
- **Çok Hafif (Çok Hafif Alzheimer)**
- **Hafif (Hafif Alzheimer)**
- **Orta (Orta Derece Alzheimer)**

## Veri Seti

Bu projede kullanılan veri seti şu şekilde yapılandırılmıştır:

```
/kaggle/input/medical-scan-classification-dataset/Alzheimer/Alzheimer/MRI
```

Veri seti, yukarıda belirtilen sınıflara ayrılmış MRI taramalarından oluşmaktadır. Görüntülerin ön işlenmesi için `ImageDataGenerator` kullanılmıştır. Piksel değerleri [0,1] aralığına yeniden ölçeklendirilmiş ve veri seti eğitim ve doğrulama alt kümelerine ayrılmıştır.

## Model Mimarisi

Model, aşağıdaki gibi tasarlanmış bir Sıralı Konvolüsyonel Sinir Ağı'dır (CNN):

1. **Conv2D + ReLU Aktivasyonu (32 filtre, 3x3 kernel)**
2. **MaxPooling2D (2x2 havuzlama boyutu)**
3. **Conv2D + ReLU Aktivasyonu (64 filtre, 3x3 kernel)**
4. **MaxPooling2D (2x2 havuzlama boyutu)**
5. **Conv2D + ReLU Aktivasyonu (128 filtre, 3x3 kernel)**
6. **MaxPooling2D (2x2 havuzlama boyutu)**
7. **Flatten Katmanı**
8. **Dense Katmanı (128 birim, ReLU aktivasyonu)**
9. **Dense Çıkış Katmanı (Softmax aktivasyonlu 4 sınıf)**

Model şu şekilde derlenmiştir:
- **Optimizasyon:** Adam
- **Kayıp Fonksiyonu:** Categorical Crossentropy
- **Metrikler:** Doğruluk

## Eğitim ve Doğrulama

- **Eğitim Alt Kümesi:** Veri setinin %90'ı
- **Doğrulama Alt Kümesi:** Veri setinin %10'u
- **Batch Boyutu:** 32
- **Görüntü Boyutu:** 150x150 piksel
- **Epok Sayısı:** 10

`ImageDataGenerator`, gerçek zamanlı veri artırma sağlar ve aşırı öğrenmeyi önlemek için verileri eğitim ve doğrulama kümelerine ayırır.

## Sonuçlar

Eğitim sırasında doğruluk ve doğrulama doğruluğu, 10 epok boyunca şu şekilde çizilmiştir:

![Doğruluk Grafiği](path-to-accuracy-plot)

### Örnek Tahminler

Modelin doğrulama veri seti üzerindeki tahminleri, gerçek etiketlerle birlikte görüntülenmiştir. Aşağıda bir örnek verilmiştir:

| Tahmin Edilen Sınıf       | Gerçek Sınıf         |
|---------------------------|----------------------|
| Çok Hafif Alzheimer       | Çok Hafif Alzheimer  |
| Hafif Alzheimer           | Hafif Alzheimer      |
| Yok                       | Yok                  |
| Orta Alzheimer            | Orta Alzheimer       |

![Örnek Tahminler](path-to-sample-predictions)

## Kullanım

1. Bu depoyu klonlayın:

   ```bash
   git clone https://github.com/your-username/alzheimer-mri-classification.git
   cd alzheimer-mri-classification
   ```

2. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install tensorflow matplotlib numpy
   ```

3. Veri setini hazırlayın:

   Veri setinin şu şekilde organize edildiğinden emin olun:

   ```
   /MRI/
      /hafif/
      /orta/
      /yok/
      /çok hafif/
   ```

4. Eğitim scriptini çalıştırın:

   ```bash
   python train_model.py
   ```

5. Sonuçları ve tahminleri görselleştirmek için değerlendirme scriptini çalıştırın:

   ```bash
   python evaluate_model.py
   ```

## Gelecek Çalışmalar

- Daha fazla sınıf veya veri seti desteği eklenmesi.
- Gelişmiş veri artırma tekniklerinin dahil edilmesi.
- VGG16 veya ResNet gibi önceden eğitilmiş modeller kullanılarak transfer öğrenme yapılması.

## Katkıda Bulunun

Katkılar memnuniyetle karşılanır! İyileştirmeler veya ek özellikler için sorunlar açabilir veya pull request gönderebilirsiniz.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakabilirsiniz.

## Teşekkürler

- **Veri Seti:** Kaggle Tıbbi Tarama Sınıflandırma Veri Seti
- **Framework ve Kütüphaneler:** TensorFlow, Keras, Matplotlib, NumPy

