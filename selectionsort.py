#////////////////////////////#
#The selection sort algorithm sorts an array by repeatedly finding the minimum element
#(considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

#1) The subarray which is already sorted.
#2) Remaining subarray which is unsorted.

#In every iteration of selection sort, the minimum element (considering ascending order)
# from the unsorted subarray is picked and moved to the sorted subarray.
#////////////////////////////#
import  time
import random


def selection_sort(data,drawData,timeTick):
    # This value of i corresponds to how many values were sorted
    for i in range(len(data)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(data)):
            if data[j] < data[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        data[i], data[lowest_value_index] = data[lowest_value_index], data[i]
        colors = ["red", "indian red"]
        drawData(data, ['green' if x == j or x == j+1 else random.choice(colors) for x in range(len(data))] )
        time.sleep(timeTick)
    drawData(data, ['gray10' for x in range(len(data))])
