# -*- coding: utf-8 -*-
"""Deep Learning: Mastering Neural Networks - Module 2 Assignment: Wine Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NX1ETyALy36Odsfs7YBLRefiRgoaQTDO

# Module 2 Assignment: Wine Classification

In this notebook we will revisit our binary classification problem, but this time we will be classifying a real world dataset!

The dataset we have chosen for this assignment is the wine quality dataset (https://archive.ics.uci.edu/ml/datasets/wine+quality). These datasets include information on over 6000 bottles of red and white wine. Your task is to develop a Single Neuron Classifier that can discern between white and red wine with a reasonable accuracy. We have provided code below for assistance with uploading the files and preparing the dataset (this is a good chance for you to learn more Python by example). Additionally we have included the final function calls we would like you to run to train and evaluate your classifier. Feel free to re-use code you have already written or seen in previous notebooks!
"""

# Download the wine .csv files from data archive
!rm -f winequality-red.csv winequality-white.csv
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv

# These are the packages required for this assignment
import pandas as pd
import numpy as np

# Use Pandas to read the csv file into a dataframe.
# Note that the delimiter in this csv is the semicolon ";" instead of a ,
df_red = pd.read_csv('winequality-red.csv',delimiter=";")

# Because we are performing a classification task, we will assign all red wine a label of 1
df_red["color"] = 1

# The method .head() is super useful for seeing a preview of our data!
df_red.head()

df_white = pd.read_csv('winequality-white.csv',delimiter=";")
df_white["color"] = 0  #assign white wine the label 0
df_white.head()

# Now we combine our two dataframes
df = pd.concat([df_red, df_white])

# And shuffle them in place to mix the red and white wine data together
df = df.sample(frac=1).reset_index(drop=True)
df.head()

# We choose three attributes of the wine to perform our prediction on
input_columns = ["citric acid", "residual sugar", "total sulfur dioxide"]
output_columns = ["color"]

# We extract the relevant features into our X and Y numpy arrays
X = df[input_columns].to_numpy()
Y = df[output_columns].to_numpy()
print("Shape of X:", X.shape)
print("Shape of Y:", Y.shape)
in_features = X.shape[1]

# Your Code Here!

# classification_model = ...

# train the model...
learning_rate = 0.001
epochs = 200
#...

# We will use this function to evaluate how well our trained classifier perfom
# Hint: the model you define above must have a .forward function in order to be compatible
# Hint: this evaluation function is identical to those in previous notebooks
def evaluate_classification_accuracy(model, input_data, labels):
    # Count the number of correctly classified samples given a set of weights
    correct = 0
    num_samples = len(input_data)
    for i in range(num_samples):
        x = input_data[i,...]
        y = labels[i]
        y_predicted = model.forward(x)
        label_predicted = 1 if y_predicted > 0.5 else 0
        if label_predicted == y:
            correct += 1
    accuracy = correct / num_samples
    print("Our model predicted", correct, "out of", num_samples,
          "correctly for", accuracy*100, "% accuracy")
    return accuracy

