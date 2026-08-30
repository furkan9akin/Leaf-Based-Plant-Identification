from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def kerass(resim):
    np.set_printoptions(suppress=True)

    model = load_model("plant_village_model.h5", compile=False)

    data = np.ndarray(shape=(1, 128, 128, 3), dtype=np.float32)

    image = Image.open(resim).convert("RGB")

    size = (128, 128)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = image_array.astype(np.float32) / 255.0

    data[0] = normalized_image_array

    prediction = model.predict(data, verbose=0)

    results = []

    for value in prediction[0]:
        results.append(round(float(value), 10))

    return results

if __name__ == "__main__":
    x = kerass("static/img/tarim_bitki.jpg")
    print(x)
