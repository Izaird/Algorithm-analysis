from matplotlib import pyplot as plt
import numpy as np 


lists = [] 
axis_x = []

filepath = 'data'
with open(filepath, "r") as fp:
   line = fp.readline()
   line = line[:-3]
   while line:
       lists.append(list(map(int,(line.split(",")))))
       line = fp.readline()
       line = line[:-3]


axis_x = np.arange(0,100000,1000)

graphs = ["Best case", "Worst case" , "Random case"]
insert_sort = 0
bubble_sort = 3
for graph in graphs:
    plt.style.use("fivethirtyeight")
    plt.plot(axis_x, lists[insert_sort],label = "Insert sort")
    plt.plot(axis_x, lists[bubble_sort],label = "Bubble sort")
    plt.xlabel("Number of items per document")
    plt.ylabel("Time in miliseconds")
    plt.title(graph)
    plt.legend()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
    insert_sort +=1
    bubble_sort +=1

