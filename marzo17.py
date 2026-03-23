import tkinter as tk
from tkinter import simpledialog, messagebox
try:
    import numpy as np
except ImportError:
    messagebox.showerror("Error", "NumPy no está instalado. Instálalo con: pip install numpy")

class MatrixMultiplierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplicador de Matrices")
        self.root.geometry("400x300")
        
        self.matrix1 = None
        self.matrix2 = None
        self.result = None
        
        # Frame principal
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(main_frame, text="Multiplicador de Matrices", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Botón para ingresar dimensiones
        self.btn_dimensions = tk.Button(main_frame, text="Ingresar Dimensiones", command=self.get_dimensions, width=30, bg="lightblue")
        self.btn_dimensions.pack(pady=10)
        
        # Botón para ingresar datos
        self.btn_data = tk.Button(main_frame, text="Ingresar Datos de Matrices", command=self.get_matrix_data, width=30, bg="lightgreen", state=tk.DISABLED)
        self.btn_data.pack(pady=10)
        
        # Botón para multiplicar
        self.btn_multiply = tk.Button(main_frame, text="Multiplicar Matrices", command=self.multiply_matrices, width=30, bg="lightyellow", state=tk.DISABLED)
        self.btn_multiply.pack(pady=10)
        
        # Botón para mostrar resultado
        self.btn_show = tk.Button(main_frame, text="Mostrar Resultado", command=self.show_result, width=30, bg="lightcoral", state=tk.DISABLED)
        self.btn_show.pack(pady=10)
        
        # Información
        self.info_label = tk.Label(main_frame, text="", fg="blue")
        self.info_label.pack(pady=10)
    
    def get_dimensions(self):
        try:
            # Ingresar dimensiones de matriz 1
            m1 = simpledialog.askinteger("Matriz 1", "Ingrese filas de Matriz 1:", minvalue=1)
            if m1 is None:
                return
            n1 = simpledialog.askinteger("Matriz 1", "Ingrese columnas de Matriz 1:", minvalue=1)
            if n1 is None:
                return
            
            # Ingresar dimensiones de matriz 2
            m2 = simpledialog.askinteger("Matriz 2", "Ingrese filas de Matriz 2:", minvalue=1)
            if m2 is None:
                return
            n2 = simpledialog.askinteger("Matriz 2", "Ingrese columnas de Matriz 2:", minvalue=1)
            if n2 is None:
                return
            
            # Verificar si se pueden multiplicar
            if n1 != m2:
                messagebox.showerror("Error", f"No se pueden multiplicar.\nColumnas de M1 ({n1}) ≠ Filas de M2 ({m2})")
                return
            
            self.dims = [(m1, n1), (m2, n2)]
            self.info_label.config(text=f"M1: {m1}x{n1} | M2: {m2}x{n2} | Resultado: {m1}x{n2}")
            self.btn_data.config(state=tk.NORMAL)
            messagebox.showinfo("Éxito", "Las dimensiones son válidas para multiplicación")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def get_matrix_data(self):
        try:
            m1_rows, m1_cols = self.dims[0]
            m2_rows, m2_cols = self.dims[1]
            
            # Ingresar datos Matriz 1
            self.matrix1 = []
            for i in range(m1_rows):
                row_str = simpledialog.askstring("Matriz 1", f"Fila {i+1} (ingrese valores separados por espacio):")
                if row_str is None:
                    return
                row = list(map(float, row_str.split()))
                if len(row) != m1_cols:
                    messagebox.showerror("Error", f"Fila {i+1} debe tener {m1_cols} valores")
                    return
                self.matrix1.append(row)
            
            # Ingresar datos Matriz 2
            self.matrix2 = []
            for i in range(m2_rows):
                row_str = simpledialog.askstring("Matriz 2", f"Fila {i+1} (ingrese valores separados por espacio):")
                if row_str is None:
                    return
                row = list(map(float, row_str.split()))
                if len(row) != m2_cols:
                    messagebox.showerror("Error", f"Fila {i+1} debe tener {m2_cols} valores")
                    return
                self.matrix2.append(row)
            
            self.btn_multiply.config(state=tk.NORMAL)
            messagebox.showinfo("Éxito", "Datos ingresados correctamente")
        
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def multiply_matrices(self):
        try:
            m1 = np.array(self.matrix1)
            m2 = np.array(self.matrix2)
            self.result = np.dot(m1, m2)
            self.btn_show.config(state=tk.NORMAL)
            messagebox.showinfo("Éxito", "Matrices multiplicadas correctamente")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error en multiplicación: {str(e)}")
    
    def show_result(self):
        if self.result is not None:
            result_str = "RESULTADO:\n\n"
            for row in self.result:
                result_str += "  ".join([f"{val:10.2f}" for val in row]) + "\n"
            
            # Crear ventana para mostrar resultado
            result_window = tk.Toplevel(self.root)
            result_window.title("Resultado")
            result_window.geometry("400x300")
            
            text_widget = tk.Text(result_window, font=("Courier", 10))
            text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            text_widget.insert(1.0, result_str)
            text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixMultiplierApp(root)
    root.mainloop()
