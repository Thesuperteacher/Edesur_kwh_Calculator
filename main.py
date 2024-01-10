import tkinter as tk


def calculate_pesos():
    kwh = float(entry.get())

    # the price per kwh
    conversion_rate = 6

    # calculate the amount in dominican Pesos
    pesos = kwh * conversion_rate

    results.config(text=f"{pesos} tienes que pagar")


# creating the main window
root = tk.Tk()
root.title("Edesur no me engaña")

root.geometry("300x300")

# input the kwh
label = tk.Label(root, text="Introduce la cantidad de kWh consumido: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

# button that says calculate
calculate_button = tk.Button(root, text="Calcular", command=calculate_pesos)
calculate_button.pack()

results = tk.Label(root, text="")
results.pack()

root.mainloop()
