
import tkinter as tk
import graph
#opening tkinter codw
def submit():
  # Method to be run when submit button is clicked  
  numDucks = int(ducks_input.get())
  numTrials = int(trials_input.get())
  sectorAngle = int(sector_input.get())
  root.destroy()
  graph.graph(numDucks,numTrials,sectorAngle)
  
root = tk.Tk()
window = tk.Canvas(root,width=520,height=560)

root.title("Ducks In A Circular Pond Simulation")
root.geometry("520x600")
window.pack(expand="YES",fill ="both")
label = tk.Label(window, text="Ducks in a Circular Pond Simulation")
label.grid(row=0, column=0,padx=10,pady=10)
ducks_label = tk.Label(window, text="Enter the number of ducks:")
ducks_label.grid(row=2, column=0,pady=10)
trials_label = tk.Label(window, text="Enter the number of trials:")
trials_label.grid(row=3, column=0,pady=10)
sector_label = tk.Label(window, text="Enter sector angle:")
sector_label.grid(row=4,column=0,pady=10)
output_label = tk.Label(window, text = "")
output_label.grid(row=5,column=1)
# Entry fields for user inputs
ducks_input = tk.Entry(window)
ducks_input.grid(row=2, column=1)
trials_input = tk.Entry(window)
trials_input.grid(row=3, column=1)
sector_input = tk.Entry(window)
sector_input.grid(row=4,column=1)
# Submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=5, column=0,padx=10,pady=10)


#Actual running

tk.mainloop()