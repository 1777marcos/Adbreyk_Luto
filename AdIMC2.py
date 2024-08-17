# Importando as bibliotecas necessárias para a interface gráfica
import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        mostrar_resultado(imc)
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

# Função para mostrar o resultado em uma nova janela
def mostrar_resultado(imc):
    resultado = tk.Toplevel()
    resultado.title("Resultado IMC")
    tk.Label(resultado, text=f"Seu IMC é: {imc:.2f}", font=("Helvetica", 14)).pack(pady=20)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 35:
        categoria = "Obesidade grau I"
    elif imc < 40:
        categoria = "Obesidade grau II"
    else:
        categoria = "Obesidade grau III ou Mórbida"
    
    tk.Label(resultado, text=categoria, font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Button(resultado, text="Fechar", command=resultado.destroy).pack(pady=20)

# Inicializando a janela principal com tkinter
root = tk.Tk()
root.title("Calculadora IMC")

# Widgets de entrada do peso
tk.Label(root, text="Insira o seu peso em kg:", font=("Helvetica", 12)).pack(pady=10)
entrada_peso = tk.Entry(root)
entrada_peso.pack()

# Widgets de entrada da altura
tk.Label(root, text="Insira a sua altura em metros:", font=("Helvetica", 12)).pack(pady=10)
entrada_altura = tk.Entry(root)
entrada_altura.pack()

# Botão para calcular o IMC
botao_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=20)

# Loop principal da interface gráfica
root.mainloop()