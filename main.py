import numpy
import time

def countingSort(arr, exp, bucketsAmount):
    n = len(arr)
    output = [0] * (n)
    count = [0] * bucketsAmount

    for i in range(n):
        count[(int)((arr[i] // exp) % bucketsAmount)] += 1

    for i in range(1,bucketsAmount):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = int((arr[i] // exp) % bucketsAmount)
        indextemp = count[index] - 1
        output[int(indextemp)] = arr[i]
        count[index] -= 1
        i -= 1
    return output


arr = numpy.random.randint(1000, size=150)
max1 = max(arr)
exp=1
start=time.time_ns()
while max1/exp > 0:
    arr = countingSort(arr, exp, 10000)
    exp*=10000
radixtime = time.time_ns() - start
print(radixtime)