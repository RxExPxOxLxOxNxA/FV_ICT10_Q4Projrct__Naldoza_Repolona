from pyscript import document, display
import numpy as np
# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

# lists
days = []
absences = []

def add_data(event):
    value_input = document.getElementById("absences").value
    if value_input == "":
        return
    day = document.getElementById("day").value
    value = int(value_input)
    days.append(day)
    absences.append(value)
    show_graph(None)

# function to display the graph
def show_graph(event):
    document.getElementById("output").innerHTML = ""
    if len(days) == 0:
        return
    x = np.array(days)
    y = np.array(absences)
    # creates the actual graph
    plt.figure(facecolor='none')
    plt.plot(x, y, marker='o')
    # labels
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid(True)
    display(plt, target="output")
    plt.close()
