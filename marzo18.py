# Prompt
'''
Un programa que calcula la ganancia de una inversion inicial
después de un numero de meses, con una tasa de interés mensual dada.
El programa debe solicitar al usuario la ganancia deseada, 
la tasa de interés mensual y el número de meses.
El programa debe mostrar la inversión inicial necesaria para alcanzar la ganancia deseada.
El programa debe ejecutarse en una interfaz gráfica.
'''

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_inversion_inicial():
    """
    Calcula la inversión inicial necesaria para alcanzar una ganancia deseada.
    Fórmula: Ganancia = Inversión_Inicial * ((1 + tasa)^meses - 1)
    Despejando: Inversión_Inicial = Ganancia / ((1 + tasa)^meses - 1)
    """
    try:
        ganancia_deseada = float(entry_ganancia.get())
        tasa_mensual = float(entry_tasa.get()) / 100
        meses = int(entry_meses.get())
        
        if ganancia_deseada <= 0 or tasa_mensual < 0 or meses <= 0:
            messagebox.showerror("Error", "Los valores deben ser positivos")
            return
        
        # Cálculo de inversión inicial
        factor = (1 + tasa_mensual) ** meses - 1
        inversion_inicial = ganancia_deseada / factor
        
        # Mostrar resultado
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Inversión inicial requerida: ${inversion_inicial:.2f}\n")
        resultado_text.insert(tk.END, f"Ganancia deseada: ${ganancia_deseada:.2f}\n")
        resultado_text.insert(tk.END, f"Monto final: ${inversion_inicial + ganancia_deseada:.2f}")
        resultado_text.config(state=tk.DISABLED)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos")

def limpiar_formulario():
    """Limpia los campos de entrada"""
    entry_ganancia.delete(0, tk.END)
    entry_tasa.delete(0, tk.END)
    entry_meses.delete(0, tk.END)
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)
    resultado_text.config(state=tk.DISABLED)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Inversión Inicial")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Marco principal
frame_principal = ttk.Frame(ventana, padding="20")
frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Título
titulo = ttk.Label(frame_principal, text="Calculadora de Inversión Inicial", 
                   font=("Arial", 14, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Ganancia deseada
ttk.Label(frame_principal, text="Ganancia deseada ($):").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_ganancia = ttk.Entry(frame_principal, width=25)
entry_ganancia.grid(row=1, column=1, sticky=tk.W, pady=5)

# Tasa de interés
ttk.Label(frame_principal, text="Tasa de interés mensual (%):").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_tasa = ttk.Entry(frame_principal, width=25)
entry_tasa.grid(row=2, column=1, sticky=tk.W, pady=5)

# Número de meses
ttk.Label(frame_principal, text="Número de meses:").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_meses = ttk.Entry(frame_principal, width=25)
entry_meses.grid(row=3, column=1, sticky=tk.W, pady=5)

# Marco de botones
frame_botones = ttk.Frame(frame_principal)
frame_botones.grid(row=4, column=0, columnspan=2, pady=15)

# Botón Calcular
btn_calcular = ttk.Button(frame_botones, text="Calcular", command=calcular_inversion_inicial)
btn_calcular.pack(side=tk.LEFT, padx=5)

# Botón Limpiar
btn_limpiar = ttk.Button(frame_botones, text="Limpiar", command=limpiar_formulario)
btn_limpiar.pack(side=tk.LEFT, padx=5)

# Texto de resultado
ttk.Label(frame_principal, text="Resultado:").grid(row=5, column=0, sticky=tk.W, pady=(10, 5))
resultado_text = tk.Text(frame_principal, height=6, width=40, state=tk.DISABLED)
resultado_text.grid(row=6, column=0, columnspan=2, pady=5)

# Ejecutar aplicación
ventana.mainloop()
