#import Numpy using the np alias, wich id a common conversation that saves you a few strokes
import numpy as np

CURVE_CENTER = 80
#create NumPy array? which is one dimensional amd has a shape of (8, and a dtd type int64
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])


def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


print(curve(grades))
