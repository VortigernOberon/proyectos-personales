# ==========================================
# ARCHIVO: interfaz.py
# ==========================================
import tkinter as tk
from tkinter import ttk, messagebox

# Importamos directamente las funciones de tu código original
from calculator import imc, altura_cm, peso_grs


# --- Funciones puente entre la GUI y tu lógica ---

def ejecutar_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        # Invocamos tu función original
        resultado = imc(peso, altura)
        
        if resultado is not None and resultado > 0:
            lbl_res_imc.config(text=f"Tu IMC es: {resultado:.2f}", fg="green")
        else:
            messagebox.showwarning("Atención", "No pueden ser valores menores o iguales a 0.")
    except ValueError:
        messagebox.showerror("Error", "Solo puedes ingresar números válidos.")


def ejecutar_altura():
    try:
        altura = float(entry_altura_solo.get())
        
        # Invocamos tu función original
        resultado = altura_cm(altura)
        
        if resultado is not None and resultado > 0:
            lbl_res_cm.config(text=f"Tu altura en CM es: {resultado:.2f} cm", fg="green")
        else:
            messagebox.showwarning("Atención", "No se puede calcular una altura menor o igual a 0.")
    except ValueError:
        messagebox.showerror("Error", "Solo puedes ingresar números válidos.")


def ejecutar_peso():
    try:
        peso = float(entry_peso_solo.get())
        
        # Invocamos tu función original
        resultado = peso_grs(peso)
        
        if resultado is not None and resultado > 0:
            lbl_res_grs.config(text=f"Tu peso en gramos es: {resultado:.2f} grs", fg="green")
        else:
            messagebox.showwarning("Atención", "No se puede calcular un peso menor o igual a 0.")
    except ValueError:
        messagebox.showerror("Error", "Solo puedes ingresar números válidos.")


# --- Construcción de la Ventana ---

ventana = tk.Tk()
ventana.title("Calculadora IMC y Conversores")
ventana.geometry("380x300")
ventana.resizable(False, False)

# Estructura de pestañas
pestanas = ttk.Notebook(ventana)
pestanas.pack(pady=10, expand=True, fill="both")

# 1. Pestaña IMC
tab_imc = ttk.Frame(pestanas)
pestanas.add(tab_imc, text="Calcular IMC")

ttk.Label(tab_imc, text="Peso en KG:").pack(pady=(15, 2))
entry_peso = ttk.Entry(tab_imc, justify="center")
entry_peso.pack(pady=2)

ttk.Label(tab_imc, text="Altura en Mts:").pack(pady=(10, 2))
entry_altura = ttk.Entry(tab_imc, justify="center")
entry_altura.pack(pady=2)

btn_calcular_imc = ttk.Button(tab_imc, text="Calcular IMC", command=ejecutar_imc)
btn_calcular_imc.pack(pady=12)

lbl_res_imc = tk.Label(tab_imc, text="", font=("Arial", 10, "bold"))
lbl_res_imc.pack()

# 2. Pestaña Metros a CM
tab_cm = ttk.Frame(pestanas)
pestanas.add(tab_cm, text="Mts a CM")

ttk.Label(tab_cm, text="Altura en Mts:").pack(pady=(25, 2))
entry_altura_solo = ttk.Entry(tab_cm, justify="center")
entry_altura_solo.pack(pady=2)

btn_calcular_cm = ttk.Button(tab_cm, text="Calcular CM", command=ejecutar_altura)
btn_calcular_cm.pack(pady=15)

lbl_res_cm = tk.Label(tab_cm, text="", font=("Arial", 10, "bold"))
lbl_res_cm.pack()

# 3. Pestaña KG a Gramos
tab_grs = ttk.Frame(pestanas)
pestanas.add(tab_grs, text="KG a Gramos")

ttk.Label(tab_grs, text="Peso en KG:").pack(pady=(25, 2))
entry_peso_solo = ttk.Entry(tab_grs, justify="center")
entry_peso_solo.pack(pady=2)

btn_calcular_grs = ttk.Button(tab_grs, text="Calcular Gramos", command=ejecutar_peso)
btn_calcular_grs.pack(pady=15)

lbl_res_grs = tk.Label(tab_grs, text="", font=("Arial", 10, "bold"))
lbl_res_grs.pack()

ventana.mainloop()