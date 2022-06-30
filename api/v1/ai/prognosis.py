import pickle
import numpy as np
class prognosis:
    def __init__(self,filename):
        self.filename=filename
        print(self.filename)
        with open(filename, 'rb') as file:
            self.p = pickle.load(file)

    def ten_years_death(self,attributes):

        attributes=np.array(attributes)
        attributes=attributes.reshape(1,-1)
        perc= self.p.predict_proba(attributes)

        return perc[0][0]
    def Diabetic_Retinopathy(self,input):
        mean = [4.091386, 4.607175, 4.499730, 4.606881]
        std = [0.141238, 0.105746, 0.106699, 0.103411]
        Data_input = []
        for i in range(4):
            Data_input.append((np.log(input[i]) - mean[i]) / std[i])

        Age_x_Systolic_BP = Data_input[0] * Data_input[1]
        Data_input.append(Age_x_Systolic_BP)
        Age_x_Diastolic_BP = Data_input[0] * Data_input[2]
        Data_input.append(Age_x_Diastolic_BP)
        Age_x_Cholesterol = Data_input[0] * Data_input[3]
        Data_input.append(Age_x_Cholesterol)
        Systolic_BP_x_Diastolic_BP = Data_input[1] * Data_input[2]
        Data_input.append(Systolic_BP_x_Diastolic_BP)
        Systolic_BP_x_Cholesterol = Data_input[1] * Data_input[3]
        Data_input.append(Systolic_BP_x_Cholesterol)
        Diastolic_BP_x_Cholesterol = Data_input[2] * Data_input[3]
        Data_input.append(Diastolic_BP_x_Cholesterol)
        print(Data_input)
        ans = self.p.predict_proba([Data_input])

        return ans[0][1]

    def prepare(img):
        IMG_SIZE = 224  # 50 in txt-based
        img_array = cv2.imread(img)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(1, IMG_SIZE, IMG_SIZE, 3)
    def chest(img):
        CATEGORIES = ['PNEUMONIA', 'NORMAL']
        prediction = model.predict([prepare(imgpath)])
        return  CATEGORIES[np.argmax(prediction)]
    def brain(img):
        CATEGORIES = ['PITUITARY', 'NOTUMOR','MENINGGIOMA', 'GLIOMA']
        prediction = model.predict([prepare(imgpath)])
        return CATEGORIES[np.argmax(prediction)]


