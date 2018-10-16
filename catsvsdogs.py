from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image

clf = Sequential()

clf.add(Convolution2D(32,3,3,input_shape = (64 , 64 , 3),activation = 'relu' ))
clf.add(MaxPooling2D(pool_size = (2,2)))
clf.add(Flatten())
clf.add(Dense(output_dim = 128,activation = 'relu'))
clf.add(Dense(output_dim = 1,activation = 'sigmoid'))
clf.compile(optimizer = 'adam' , loss = 'binary_crossentropy' , metrics = ['accuracy'])

train_datagen = ImageDataGenerator( rescale=1./255, shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

trainingset = train_datagen.flow_from_directory('dataset/training_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='binary')

testset = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

clf.fit_generator(trainingset,
                  steps_per_epoch=8000,
                  epochs=25,
                  validation_data=testset,
                  validation_steps=2000)


test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = clf.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'
