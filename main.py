from numpy import random

def sort(arr):
    arr.sort()
    arr[[0,2]] = arr[[2,0]] #swap test
    print("Sorting:", " ", arr)

sort(random.randint(1,30,20))