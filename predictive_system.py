import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open(r'E:\Data Science\Projects\02. Diabites Prediction\trained_model.sav', 'rb'))

input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)
input_data_as_numpy_array = np.asarray(input_data)
# Reshaping the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Standardizing the input data

prediction = loaded_model.predict(input_data_reshaped)
if prediction[0] == 0:
    print("The person is not diabetic")
else:
    print("The person is diabetic")

