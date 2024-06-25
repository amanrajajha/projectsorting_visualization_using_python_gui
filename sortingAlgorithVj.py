from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quickSort import quick_sort
from mergesort import merge_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort
from tkinter import *





root=Tk()
root.title('sorting Algorith Visualisation')#title of out app
root.maxsize(1000, 800)  #this tells us about the maximum size of our gui app made in tk
root.config(bg='pink') #this gives the background color

#variable
selected_alg = StringVar()
data=[]
#drawdata function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()
#to generate data from entered value
def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    drawData(data, [random.choice(colors)  for x in range(len(data))]) #['red', 'red' ,....]

#function to implement given
def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'insertion Sort':
        insertion_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'selection Sort':
        selection_sort(data, drawData, speedScale.get())







UI_frame=Frame(root,width=600,height=300,bg='orange')
UI_frame.grid(row=0,column=0,padx=10,pady=5)
#canvas for drawing
canvas= Canvas(root,width=650,height=450,bg='wheat2')
canvas.grid(row=1,column=0,padx=10,pady=5)


#user interface are
#row[0]
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='indian red').grid(row=0, column=0, padx=5, pady=5, sticky=W)#sticky parameter in west
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Quick Sort', 'Merge Sort','insertion Sort','selection Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)



speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]",bg='indian red')
speedScale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_frame,text="START", command=StartAlgorithm,bg='yellow').grid(row=0, column=3, padx=5, pady=5)

#row[1]
sizeEntry = Scale(UI_frame, from_=3, to=45, resolution=1, orient=HORIZONTAL, label="Data Size",bg='indian red')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value",bg='indian red')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value",bg='indian red')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

#row[2]
Label(UI_frame, text="This project is created by VISHESH JHA", bg='indian red').grid(row=2, column=1, padx=5, pady=5, sticky=W)

root.mainloop()
