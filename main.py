import numpy
import time


def countingSort(arr, exp, bucketsAmount):
    n = len(arr)
    output = [0] * (n)
    count = [0] * bucketsAmount

    # puts numbers in desired buckets
    for i in range(n):
        count[(int)((arr[i] // exp) % bucketsAmount)] += 1

    for i in range(1, bucketsAmount):
        count[i] += count[i - 1]

    # creates (semi)sorted output array
    i = n - 1
    while i >= 0:
        index = int((arr[i] // exp) % bucketsAmount)
        indextemp = count[index] - 1
        output[int(indextemp)] = arr[i]
        count[index] -= 1
        i -= 1
    return output


# create random array(length=150, range=0,1000)
arr = numpy.random.randint(1000, size=150)
# finds max number in array
max1 = max(arr)
exp = 1
base = 10000

# starts counting sort completion time
start = time.time_ns()
# radixes through numbers in base 10000
while max1 / exp > 0:
    arr = countingSort(arr, exp, base)
    exp *= base
# calculates time it took to complete sort
radixtime = time.time_ns() - start
print(radixtime)
