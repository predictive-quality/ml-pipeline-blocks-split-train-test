# Copyright (c) 2022 RWTH Aachen - Werkzeugmaschinenlabor (WZL)
# Contact: Simon Cramer, s.cramer@wzl-mq.rwth-aachen.de

from absl import app, flags,logging
from split_train_test import split_train_test

FLAGS = flags.FLAGS

flags.DEFINE_string('input_path',default=None,help='Path where feature files in feahter format were found')
flags.DEFINE_string('output_path',default=None,help='Path where scaled features in feather format were stored')
flags.DEFINE_string('filename_x',default=None,help='Name of the file which should be splitted into train and test.')
flags.DEFINE_string('filename_y',default=None,help='Optional. Name of the file which should be splitted into train and test relating to filename_x.')
flags.DEFINE_boolean('shuffle',default=True,help='Whether or not to shuffle the data before splitting. If shuffle=False then stratify must be None.')
flags.DEFINE_float('test_size',default=0.1,help='If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.')

flags.mark_flag_as_required('input_path')
flags.mark_flag_as_required('output_path')
flags.mark_flag_as_required('filename_x')

def main(argv):
    """This function reads pandas Dataframes from an input path and splits them into test and train dataframes.

    """    
    del argv

    if FLAGS.test_size > 1.0 or FLAGS.test_size < 0.0:
        logging.warning('Test Size is not between range of 0.0 - 1.0!')
    else:
        split_train_test(FLAGS.input_path,FLAGS.output_path,FLAGS.filename_x,FLAGS.filename_y,FLAGS.shuffle,FLAGS.test_size)



if __name__ == '__main__':
    app.run(main)