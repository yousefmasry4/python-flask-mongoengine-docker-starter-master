import numpy as np
import  cv2
import tensorflow as tf
class diagnosis:
    def __init__(self,filename):
        self.filename=filename
        self.model = tf.keras.models.load_model("chestv2.h5")

    @staticmethod
    def prepare(img):
        IMG_SIZE = 224
        img_array = cv2.imread(img)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(1, IMG_SIZE, IMG_SIZE, 3)
    def chest(self,img):
        CATEGORIES = ['PNEUMONIA', 'NORMAL']
        prediction = self.model.predict([self.prepare(img)])
        return  CATEGORIES[np.argmax(prediction)]
    def brain(self,img):
        CATEGORIES = ['PITUITARY', 'NOTUMOR','MENINGGIOMA', 'GLIOMA']
        prediction = self.model.predict([self.prepare(img)])
        return CATEGORIES[np.argmax(prediction)]


mychestmodel= diagnosis("chestv2.h5")
print(mychestmodel.chest("person1656_virus_2862.jpeg"))