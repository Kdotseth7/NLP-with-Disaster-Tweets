# Load data into a DataFrame
from pandas import read_csv


def dataset():
    train = read_csv("../../data/train.csv")
    test = read_csv("../../data/test.csv")
    return train, test
