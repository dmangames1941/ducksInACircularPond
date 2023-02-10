import tkinter as tk
import Simulation as sim

def submit():
  # Method to be run when submit button is clicked
  numDucks = int(ducks_input.get())
  numTrials = int(trials_input.get())
  sectorAngle = int(sector_input.get())

  relFreq = sim.Simulation(numDucks, numTrials, sectorAngle)


root = tk.Tk()
root.title("Ducks In A Circular Pond Simulation")
root.geometry("500x300")

label = tk.Label(root, text="Ducks in a Circular Pond Simulation")
label.grid(row=0, column=0,padx=10,pady=10)

ducks_label = tk.Label(root, text="Enter the number of ducks:")
ducks_label.grid(row=2, column=0,pady=10)

trials_label = tk.Label(root, text="Enter the number of trials:")
trials_label.grid(row=3, column=0,pady=10)

sector_label = tk.Label(root, text="Enter sector angle:")
sector_label.grid(row=4,column=0,pady=10)

output_label = tk.Label(root, text = "")
output_label.grid(row=5,column=1)

# Entry fields for user inputs
ducks_input = tk.Entry(root)
ducks_input.grid(row=2, column=1)

trials_input = tk.Entry(root)
trials_input.grid(row=3, column=1)

sector_input = tk.Entry(root)
sector_input.grid(row=4,column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=0,padx=10,pady=10)


tk.mainloop()