# Copyright (c) 2022 RWTH Aachen - Werkzeugmaschinenlabor (WZL)
# Contact: Simon Cramer, s.cramer@wzl-mq.rwth-aachen.de

from sklearn.model_selection import train_test_split
from s3_smart_open import to_pd_fth, read_pd_fth
import pandas as pd
import os
from absl import logging

def split_train_test(input_path,output_path,filename_x,filename_y=None,shuffle=True,test_size=0.1):
    """Split pandas dataframe into train dataframe and test dataframe.

    Args:
        input_path (string): Input path for loading feather files
        output_path (string): Output path for saving feather file
        filename_x (string): Name of the file which should be splitted into train and test.
        filename_y (string): Optional. Name of the file which should be splitted into train and test relating to filename_x.
        filenames (list): List of filenames for loading feather files
        shuffle (bool): Whether or not to shuffle the data before splitting. If shuffle=False then stratify must be None.
        test_size (float): If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.
    """   

    dataframe_x = read_pd_fth(input_path,filename_x)
    if filename_y:
        dataframe_y = read_pd_fth(input_path,filename_y)
        dataframe_x_train, dataframe_x_test, dataframe_y_train, dataframe_y_test = train_test_split(dataframe_x, dataframe_y,  test_size=test_size, shuffle=shuffle)
        to_pd_fth(output_path, os.path.splitext(filename_y)[0] +'_train.fth', dataframe_y_train)
        to_pd_fth(output_path, os.path.splitext(filename_y)[0] +'_test.fth', dataframe_y_test)

    else:
        dataframe_x_train, dataframe_x_test, = train_test_split(dataframe_x, test_size=test_size, shuffle=shuffle)

    to_pd_fth(output_path, os.path.splitext(filename_x)[0] +'_train.fth',dataframe_x_train)
    to_pd_fth(output_path, os.path.splitext(filename_x)[0] +'_test.fth',dataframe_x_test)

