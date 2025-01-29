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



## Geliştirldiği Ortamlar
Kaggle ve Visual Studio Code ortamında geliştirilmiştir.
<br> 

<div align="Center">
  <img src="https://miro.medium.com/v2/resize:fit:1200/1*JSbnt_mxpFfkGtNtGbR40g.png" height="200" alt="numpy logo"  />
  <img src="https://www.justinjbird.me/images/apps/vscode.webp" height="200" alt="numpy logo"  />
<br>
</div>

## Gerekli Kütüphaneler
Proje için aşağıdaki Python kütüphaneleri gereklidir:
- TensorFlow
- NumPy
- Matplotlib
- Keras
<br>
<div align="Center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="50" alt="numpy logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="50" alt="tensorflow logo"  />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" height="50" alt="plotlib logo"  />
  <img width="12" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" height="50" alt="plotlib logo"/>
  <img width="12" />
</div>

## Keras <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" width="35" align="left">

Keras, derin öğrenme (deep learning) uygulamaları geliştirmek için kullanılan açık kaynaklı bir Python kütüphanesidir. Başlangıçta Theano ve TensorFlow gibi arka uç kütüphanelerine dayanarak çalışıyordu, ancak günümüzde TensorFlow'un yüksek seviyeli API'si olarak entegre edilmiştir. Keras, kullanıcı dostu ve modüler bir yapıya sahip olup, hızlı prototipleme, eğitim ve derin öğrenme modellerinin geliştirilmesi için idealdir.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:2400/1*36MELEhgZsPFuzlZvObnxA.gif" alt="Example GIF" height="300", width="400">
</p>

## Numpy <img src="https://numpy.org/images/logo.svg" alt="Numpy Logo" width="35" align="left">
NumPy, Python dilinde büyük sayılar ve çok boyutlu diziler üzerinde hızlı ve etkili matematiksel işlemler gerçekleştirmeye olanak sağlayan bir python kütüphanedir. NumPy, aynı zamanda Python'da matematiksel işlemler yapmak için kullanılan diğer kütüphanelerle uyumlu bir şekilde çalışır.

<p align="center">
  <img src="https://matteding.github.io/images/broadcasting-3d-scalar.gif" alt="Example GIF" height="300", width="400">
</p>

## Tensorflow <img src="https://avatars.githubusercontent.com/u/15658638?s=280&v=4" alt="Numpy Logo" width="35" align="left">
TensorFlow, makine öğrenimi için ücretsiz ve açık kaynaklı bir yazılım kütüphanesidir . Bir dizi görevde kullanılabilir, ancak derin sinir ağlarının eğitimi ve çıkarımına özel olarak odaklanmaktadır
<p align="center">
  <img src="https://www.tensorflow.org/static/site-assets/images/marketing/cards/spotify-tensorflow-agents-recommendation-systems.gif" alt="Example GIF" height="300", width="400">
</p>

## Matplotlib <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Numpy Logo" width="35" align="left">

Matplotlib, Python programlama dilinin temel çizim kitaplığıdır. Python görselleştirme paketleri arasında en yaygın kullanılanıdır.
<p align="center">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2ZvFv81XgsfhwqoAM0MOKKtzuVfhxw77xDMFd33AzpZ0ErQLp0e53PNItYnE7cbZuLYd4Ssv2CG540RE1h1nUS3PU5jLF71Zg-jYaxI5mFZXVSvZnnklptUxR3bd2VP28it24tt8op9QH/s400/plot_surface_animation_funcanimation_r.gif" height="300", width="400">
</p>



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


