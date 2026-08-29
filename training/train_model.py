import zipfile
import os
from keras.preprocessing.image import ImageDataGenerator

# Zip dosyasını çıkar
with zipfile.ZipFile('plant-village-dataset-updated.zip', 'r') as zip_ref:
    zip_ref.extractall('dataset')

model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(64, activation='relu'),
    # Changed the number of neurons in the output layer to match the number of classes in your dataset
    Dense(9, activation='softmax')
])

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

training_data = train_datagen.flow_from_directory(
    '/content/dataset',  # Klasör yolu
    target_size=(128,128),
    batch_size=16,
    class_mode='categorical',
    subset='training'  # Eğitim verisi
)
print("Class mapping:", training_data.class_indices)

# Ensure that validation data covers all 38 or 9 classes
validation_data = train_datagen.flow_from_directory(
    '/content/dataset',  # Use same path as training data or correct path containing all classes
    target_size=(128,128),
    batch_size=16,
    class_mode='categorical',
    subset='validation'  # Validasyon verisi
)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(training_data, epochs=10, validation_data=validation_data)

model.save('plant_village_model.h5')
