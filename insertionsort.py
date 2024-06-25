#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
#example
#12, 11, 13, 5, 6

#Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

#i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
#11, 12, 13, 5, 6

#i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
#11, 12, 13, 5, 6

#i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
#5, 11, 12, 13, 6

#i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
#5, 6, 11, 12, 13
import random
import time

def insertion_sort(data,drawData,timeTick):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(data)):
        # This is the element we want to position in its
        # correct place
        key_item = data[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and data[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            data[j + 1] = data[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        data[j + 1] = key_item
        colors = ["red", "indian red"]
        drawData(data, ['green' if x == j or x == j+1 else random.choice(colors) for x in range(len(data))] )
        time.sleep(timeTick)
    drawData(data, ['gray10' for x in range(len(data))])
