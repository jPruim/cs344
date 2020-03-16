"""

Lab06 part three goal
Load the Keras version of the Boston Housing Price dataset (boston_housing) and do the following:
Print the number of training and testing examples.
Print the rank (i.e., number of axes/dimensions), shape and data type of the examples.
by Jason Pruim for Calvin University, Spring 2020, CS344

"""
import sys
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/aima")
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/paip")
import numpy
from keras.datasets import boston_housing
(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()

def print_structures():
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(train_images), 
                train_images.ndim, 
                train_images.shape, 
                train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \
            \n\tvalues: {}\n'.format(
                len(test_labels), 
                train_labels.ndim, 
                test_labels.shape, 
                test_labels.dtype, 
                test_labels
        )
    )



if __name__ == "__main__":
    print_structures()

