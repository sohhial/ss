# -*- coding: utf-8 -*-
"""Teachable Machine

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13SoRYZHBT0UBHPATm7ICXFC5f5suj3MK
"""

pip install teachable-machine

pip install tensorflow pillow

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
model = load_model('keras_model.h5')
img_path = '11.PNG'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0) / 255.0
preds = model.predict(x)[0]
class_names = ['A', 'O']
predicted_index = np.argmax(preds)
predicted_class = class_names[predicted_index]
plt.imshow(img)
plt.axis('off')
plt.title(f"Predicted Class: {predicted_class}", fontsize=16)
plt.show()
print(f"Predicted class for {img_path}: {predicted_class}")

pip install tensorflow==2.12.1