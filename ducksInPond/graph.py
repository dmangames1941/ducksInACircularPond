import tkinter as tk
import Simulation as sim
import Output as o

labelString = ""

def DrawCircle(window2):
    circle = window2.create_oval(10,10,510,510)
def graph(totalDucks,iterations,angle):   
    global totalSucess
    global currentIteration
    root2 = tk.Tk()
    root2.title("Ducks In A Circular Pond Simulation")
    root2.geometry("520x650")
    window2 = tk.Canvas(root2,width=520,height=650)
    window2.pack(expand="YES",fill ="both")
    totalSucess = 0
    currentIteration = 1
    DrawCircle(window2)    
    DataLabel = tk.Label(root2, text = labelString)
    windowUpdater(root2, totalDucks,iterations, angle, window2, DataLabel)
    submit_button = tk.Button(window2,  command=lambda:[windowUpdater(root2,totalDucks,iterations,angle,window2,DataLabel)])
    DataLabel.pack(side="bottom")
    submit_button.pack(side="bottom")
    root2.mainloop()


def windowUpdater(root,totalDucks,iterations,angle,window2,DataLabel):
    global totalSucess
    global currentIteration
    clearGraph(window2)
    sim1 = sim.Simulation(totalDucks,angle)
    for i in range(len(sim1.getDuckList())):
        xDuck = sim1.getDuckList()[i].getX()
        yDuck = sim1.getDuckList()[i].getY()
        xDuck = 260+xDuck
        yDuck = 260+yDuck
        drawpoint(window2,xDuck,yDuck)
    totalSucess = totalSucess +sim1.getTotalSucess()
    DataLabel.config(text= labelMaker(totalDucks,angle,currentIteration,iterations,(totalSucess/currentIteration),DataLabel))
    DrawCircle(window2)
    
    if currentIteration <= iterations:
        currentIteration = 1+currentIteration
        root.after(1000,windowUpdater,root,totalDucks,iterations,angle,window2,DataLabel)
    else:
        root.destroy()
        o.output(totalDucks, angle, iterations, totalSucess, (totalSucess/currentIteration))
def labelMaker(totalDucks,angle,iterationsCurrent,iterationsTotal,percentageSucess,DataLabel):
    labelString = "Total Duck: "+ str(totalDucks)+",  Angle: "+ str(angle)+", Iterations: "+str(iterationsCurrent)+" Of " +str(iterationsTotal) + ",\n Number of Successes: "+ str(totalSucess) + ", Relative Frequency of Successes: "+str(percentageSucess)
    return labelString
def drawpoint(window2,x,y):
    python_green = "#476042"
    window2.create_oval(x-5, y-5, x+5, y+5, fill=python_green)
def clearGraph(canvas):
    canvas.delete('all')
    

