# import numpy as np
# from PIL import Image
# import tensorflow as tf
#
# PATH = "../kareemModel/"
#
# MODEL = tf.keras.models.load_model(PATH, compile=False)
# CLASS_NAMES = ["Pepper__bell___Bacterial_spot", "Pepper__bell___healthy", "Potato___Early_blight"]
#
#
# def read_file_as_image(data):
#     image_ = np.array(data)
#     return image_
#
#
# def class_detect(path):
#     image = Image.open(path)
#
#     image = read_file_as_image(image)
#     image.resize(256, 256, 3)
#     img_batch = np.expand_dims(image, 0)
#
#     predictions = MODEL.predict(img_batch)
#
#     predicted_class = str(CLASS_NAMES[np.argmax(predictions[0])])
#     confidence = np.max(predictions[0]) * 100
#     confidence = str("{:.2f}".format(confidence))
#
#     data = {
#         "class": predicted_class,
#         "score": confidence
#     }
#     return data

