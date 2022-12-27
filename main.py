# This is a sample Python script.
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def create_upload_file(file):

    # load model
    model = load_model('test.h5')
    # summarize model.
    #model.summary()
    # load dataset
    Image_test = file
    imagetest = image.load_img(Image_test, target_size=(150, 150))
    # image1
    input_arr = image.img_to_array(imagetest)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    input_arr
    predictions = model.predict(input_arr)
    #print(predictions)
    predictionsclasses=['diseased cotton leaf','diseased cotton plant','fresh cotton leaf','fresh cotton plant']
    probabilitiestest = list(predictions)
    testprob = max(probabilitiestest)
    #print(testprob.tolist())
    max_value = max(testprob)
    #print(max_value)
    for i in range(len(testprob)):
        if testprob[i] == max_value:
            max_index = i
    predictionslabel=predictionsclasses[max_index]
    #print(predictionslabel)
    results_final = [
        {'cottonhealthcategory': predictionslabel
         }]
    print(results_final)

    return results_final

def create_upload_files(file):

    # load model
    model = load_model('test.h5')
    # summarize model.
    #model.summary()
    # load dataset
    Image_test = file
    imagetest = image.load_img(Image_test, target_size=(150, 150))
    # image1
    input_arr = image.img_to_array(imagetest)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    input_arr
    predictions = model.predict(input_arr)
    #print(predictions)
    predictionsclasses=['diseased cotton leaf','diseased cotton plant','fresh cotton leaf','fresh cotton plant']
    probabilitiestest = list(predictions)
    testprob = max(probabilitiestest)
    #print(testprob.tolist())
    max_value = max(testprob)
    #print(max_value)
    for i in range(len(testprob)):
        if testprob[i] == max_value:
            max_index = i
    predictionslabel=predictionsclasses[max_index]
    #print(predictionslabel)
    #results_final = [
    #    {'cottonhealthcategory': predictionslabel,
    #    'diseased cotton leaf':int(testprob[0]),
    #    'diseased cotton plant':int(testprob[1]),
    #     'fresh cotton leaf':int(testprob[2]),
    #     'fresh cotton plant':int(testprob[3]),
    #     }]
    print(predictionslabel)

    return predictionslabel
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #file='test/dis_leaf (124).jpg'
    #create_upload_file(file)

    #file='test/d (378).jpg'
    #create_upload_file(file)

    #file='test/dd (328).jpg'
    #create_upload_file(file)

    #file='test/dsd (405).jpg'
    #create_upload_file(file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
