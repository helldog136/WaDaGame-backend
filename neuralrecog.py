from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

from keras.wrappers.scikit_learn import KerasClassifier


def enehanceData():
    datagen = ImageDataGenerator(
            rotation_range=0,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=False,
            fill_mode='nearest')

    for typ in os.listdir("./trainingImporter/training"):
        for path in os.listdir("./trainingImporter/training/"+typ):
            try:
                img = load_img("./trainingImporter/training/" + typ + "/" + path)  # this is a PIL image
                x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
                x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

                print str(typ) + "\t" + str(path) + "\t",
                # the .flow() command below generates batches of randomly transformed images
                # and saves the results to the `preview/` directory
                i = 0
                for batch in datagen.flow(x, batch_size=1,
                                          save_to_dir="./trainingImporter/training/"+typ, save_prefix=typ, save_format='jpg'):
                    print str(i) + "...",
                    i += 1
                    if i > 3:
                        print " Done!"
                        break  # otherwise the generator would loop indefinitely
            except Exception as e:
                if img is not None:
                    img.close()
                print ""
                print "ERROR: REMOVING CORRUPTED(?) FILE:"+typ + "/" + path
                os.remove("./trainingImporter/training/" + typ + "/" + path)

def train():
    from keras.models import Sequential
    from keras.layers import Convolution2D, MaxPooling2D
    from keras.layers import Activation, Dropout, Flatten, Dense

    model = Sequential()
    model.add(Convolution2D(32, 3, 3, input_shape=(3, 150, 150)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1, 145)))

    model.add(Convolution2D(32, 1, 1))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1, 1)))

    model.add(Convolution2D(64, 1, 1))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(1, 1)))

    # the model so far outputs 3D feature maps (height, width, features)
    model.add(Dense(4, init='normal', activation='relu'))
    model.add(Dense(4, init='normal', activation='relu'))
    model.add(Dense(3, init='normal', activation='sigmoid'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])


    # this is the augmentation configuration we will use for training
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=False)

    # this is the augmentation configuration we will use for testing:
    # only rescaling
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    # this is a generator that will read pictures found in
    # subfolers of 'data/train', and indefinitely generate
    # batches of augmented image data
    train_generator = train_datagen.flow_from_directory(
        './trainingImporter/training/',  # this is the target directory
        target_size=(3, 150, 150),  # all images will be resized to 150x150
        batch_size=32,
        class_mode='categorical',
        classes=os.listdir("./trainingImporter/training"))

    # this is a similar generator, for validation data
    validation_generator = test_datagen.flow_from_directory(
        './trainingImporter/training/',
        target_size=(3, 150, 150),
        batch_size=32,
        class_mode='categorical',
        classes=os.listdir("./trainingImporter/training"))

    model.fit_generator(
        train_generator,
        samples_per_epoch=2000,
        nb_epoch=50,
        validation_data=validation_generator,
        nb_val_samples=800)
    model.save_weights('first_try.h5')  # always save your weights after training or during training

train()
