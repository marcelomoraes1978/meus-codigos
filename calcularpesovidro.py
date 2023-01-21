import tkinter as tk

def calcular():
    largura = float(largura_entry.get())
    altura = float(altura_entry.get())
    espessura = float(espessura_entry.get())
    densidade = float(densidade_entry.get())

    volume = largura * altura * espessura
    peso = volume * densidade
    peso_label.config(text="Peso: {:.2f} kg".format(peso))

root = tk.Tk()
root.title("Calculadora de Peso de Vidro")

largura_label = tk.Label(root, text="Largura (cm)")
largura_label.pack()

largura_entry = tk.Entry(root)
largura_entry.pack()

altura_label = tk.Label(root, text="Altura (cm)")
altura_label.pack()

altura_entry = tk.Entry(root)
altura_entry.pack()

espessura_label = tk.Label(root, text="Espessura (cm)")
espessura_label.pack()

espessura_entry = tk.Entry(root)
espessura_entry.pack()

densidade_label = tk.Label(root, text="Densidade (kg/cm³)")
densidade_label.pack()

densidade_entry = tk.Entry(root)
densidade_entry.pack()

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.pack()

peso_label = tk.Label(root, text="")
peso_label.pack()

root.mainloop()
