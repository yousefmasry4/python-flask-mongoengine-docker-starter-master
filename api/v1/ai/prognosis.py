import pickle
import numpy as np
import sklearn
import os
class prognosisAi:
    def __init__(self):
        filename="/code/api/v1/ai/10-year-risk-of-death"
        with open(filename, 'rb') as file:
            self.p = pickle.load(file)
        filename2="/code/api/v1/ai/Diabetic_Retinopathy"
        with open(filename2, 'rb') as file2:
            self.p2 = pickle.load(file2)
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
        ans = self.p2.predict_proba([Data_input])

        return ans[0][1]

if __name__ == "__main__":
    a=prognosis()
    print(a.ten_years_death([1,2,3,4,5]))
    print(a.Diabetic_Retinopathy([1,2,3,4,5,6,7,8,9,1]))
