# Sklearn train_test_split
Split arrays or matrices into random train and test subsets.


## Installation

Clone the repository and install all requirements using `pip install -r requirements.txt` .


## Usage

Use `filename_x` to split a single file into train and test files. \
Use `filename_x` and `filename_y` to split two relating files into 2 train and 2 test files.

You can run the code in two ways.
1. Use command line flags as arguments `python main.py --input_path= --output_path=...`
2. Use a flagfile.txt which includes the arguments `python main.py --flagfile=example/flagfile.txt`

## Input Flags/Arguments

#### --input_path
S3 or local path where input files are stored.

#### --output_path
S3 or local path where output file will be saved.

#### --filename_x
Name of the file which should be splitted into train and test.

#### --filename_y
Optional. Name of the file which should be splitted into train and test relating to filename_x.

#### --shuffle
Whether or not to shuffle the data before splitting.

#### --test_size
Float value between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.


## Example

First move to the repository directory. \
We split a dataframe with feature values and the relating dataframe with target values with `python main.py --flagfile=flagfile.txt`.


## Data Set

The data set was recorded with the help of the Festo Polymer GmbH. The features (`x.csv`) are either parameters explicitly set on the injection molding machine or recorded sensor values. The target value (`y.csv`) is a crucial length measured on the parts. We measured with a high precision coordinate-measuring machine at the Laboratory for Machine Tools (WZL) at RWTH Aachen University.