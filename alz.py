import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
import os
base_dir = "/kaggle/input/medical-scan-classification-dataset/Alzheimer/Alzheimer/MRI"
classes = ["hafif","orta","yok","çok hafif"]
datagen = ImageDataGenerator(rescale=1.0/255.0,validation_split=0.1)
train_data = datagen.flow_from_directory(base_dir, target_size=(150, 150), batch_size=32, class_mode='categorical',subset='training')
test_data = datagen.flow_from_directory(
    base_dir, target_size=(150, 150), batch_size=32,class_mode='categorical', subset='validation')
model = models.Sequential([layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D((2, 2)),layers.Conv2D(64, (3, 3), activation='relu'),layers.MaxPooling2D((2, 2)),layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(), layers.Dense(128, activation='relu'),
    layers.Dense(len(classes), activation='softmax')])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, validation_data=test_data, epochs=10)
plt.plot(history.history['accuracy'], label='Eğitim Doğruluk Oranı')
plt.plot(history.history['val_accuracy'], label='Test Doğruluk Oranı')
plt.title('Model Doğruluk Oranı')
plt.xlabel('Epok(Epoch)')
plt.ylabel('Doğruluk oranı')
plt.legend()
plt.show()
test_images, test_labels = next(test_data)
predictions = model.predict(test_images)
plt.figure(figsize=(40, 20))
for index in range(20):
    plt.subplot(4, 5, index + 1) 
    plt.imshow(test_images[index])
    plt.title(f"Tahmin: {classes[np.argmax(predictions[index])]} \nGerçek: {classes[np.argmax(test_labels[index])]}", fontsize=30)
    plt.subplots_adjust(hspace=0.7, wspace=0.3)
    plt.axis('off')  
plt.show()