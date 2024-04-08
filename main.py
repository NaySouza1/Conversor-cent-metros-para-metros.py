import tkinter as tk

def converter_cm_para_m():
    try:
        cm = float(entrada_cm.get())
        metros = cm / 100
        resultado_label.config(text=f"{cm} centímetros equivalem a {metros} metros.")
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido.")

# janela
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")

# Rótulo para o título
titulo_label = tk.Label(janela, text="Conversor Centímetros para Metros", font=("Arial", 14))
titulo_label.pack()

# rótulo e campo de entrada centímetros
tk.Label(janela, text="Insira o valor em centímetros que deseja converter:").pack()
entrada_cm = tk.Entry(janela)
entrada_cm.pack()

# converter
botao_converter = tk.Button(janela, text="Converter", command=converter_cm_para_m)
botao_converter.pack()

# resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()
