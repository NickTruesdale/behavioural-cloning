'''
This module implements a Keras CNN.
'''

import os
from typing import List

import pandas as pd
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Lambda, Conv2D, Dropout, Dense, Flatten, Activation, BatchNormalization
from keras.activations import elu
#from keras.optimizers import Adam

# Options - move to a config or .env file at some point
IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 66, 200, 3
INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)


def create_model(dropout: float = 0.5):
    ''' 
    This is an implementation of the NVIDIA CNN with the following layers:
    - Image normalization (to avoid saturation and make gradients work better)
    - Convolution: 5x5, filter: 24, strides: 2x2, activation: ELU
    - Convolution: 5x5, filter: 36, strides: 2x2, activation: ELU
    - Convolution: 5x5, filter: 48, strides: 2x2, activation: ELU
    - Convolution: 3x3, filter: 64, strides: 1x1, activation: ELU
    - Convolution: 3x3, filter: 64, strides: 1x1, activation: ELU
    - Drop out (0.5)
    - Fully connected: neurons: 100, activation: ELU
    - Fully connected: neurons: 50, activation: ELU
    - Fully connected: neurons: 10, activation: ELU
    - Fully connected: neurons: 1 (output)

    Roughly, the convolutional layers do feature extraction and the fully connected
    layers do steering prediction. ELU is used to solve the vanishing gradient problem.
    '''
    
    def process_layer(layer):
        '''
        For each layer that can take an activation function, assign the ELU function and add a
        Batch Normalization layer after to help keep training time down.
        '''
        if 'activation' in layer.get_config():
            layer.activation = elu
            return [layer, BatchNormalization()]
        else:
            return [layer]

    layers = [
        Lambda(lambda x: x/127.5-1.0, input_shape=INPUT_SHAPE),
        Conv2D(24, 5, strides=2),
        Conv2D(36, 5, strides=2),
        Conv2D(48, 5, strides=2),
        Conv2D(64, 3),
        Conv2D(64, 3),
        Dropout(dropout),
        Flatten(),
        Dense(100),
        Dense(50),
        Dense(10),
        Dense(1)
    ]

    # Change activation to ELU and add a BN layer after each conv and dense layer (except the last)
    layers = [L for layer in layers[:-1] for L in process_layer(layer)].append(layers[-1])
    model = Sequential(layers)
    return model


def load_data():
    """
    Load training data and split it into training and validation set
    """
    #reads CSV file into a single dataframe variable
    data_dir = '../data'
    data_file = os.path.join(os.getcwd(), data_dir, 'driving_log.csv')
    column_names = ['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed']
    
    data_df = pd.read_csv(data_file, names=column_names)

    # Split dataframe into features (cameras) and labels (steering output)
    X = data_df[['center', 'left', 'right']].values
    y = data_df['steering'].values

    # Split data into training and testing sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)

    return X_train, X_test, y_train, y_test

