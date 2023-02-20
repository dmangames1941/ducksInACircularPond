import tkinter as tk


def output(totalDucks,angle,iterations, totalSucess, percentageSucess):
    root = tk.Tk()
    root.title("Ducks In A Circular Pond Simulation")
    root.geometry("520x650")
    window = tk.Canvas(root,width=520,height=650)
    window.pack(expand="YES",fill ="both")

    label = tk.Label(window, text="Results")
    label.pack(side="top")

    resultLabel = tk.Label(window, text = "Total Duck: "+ str(totalDucks)+"\nAngle: "+ str(angle)+"\nNumber of Iterations: " + str(iterations) + "\nNumber of Successes: "+ str(totalSucess) + "\nRelative Frequency of Successes: "+str(percentageSucess))
    resultLabel.pack()
    
    root.mainloop()