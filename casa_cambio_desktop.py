import customtkinter as ctk
from tkinter import messagebox
import requests
from datetime import datetime
import threading

class CasaCambioApp:
    def __init__(self):
        # Configuración inicial
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("Casa de Cambio MXN ↔ USD")
        self.root.geometry("500x650")
        
        # Variables
        self.tipo_cambio = 17.5  # Tipo de cambio por defecto
        self.ultima_actualizacion = "Manual"
        
        # Crear interfaz
        self.crear_interfaz()
        
        # Obtener tipo de cambio real al iniciar
        self.obtener_tipo_cambio()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame, 
            text="🏦 Casa de Cambio",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(20, 10))
        
        # Subtítulo
        subtitle_label = ctk.CTkLabel(
            main_frame,
            text="Pesos Mexicanos ↔ Dólares Estadounidenses",
            font=ctk.CTkFont(size=14)
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Frame del tipo de cambio
        exchange_frame = ctk.CTkFrame(main_frame)
        exchange_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        ctk.CTkLabel(
            exchange_frame,
            text="Tipo de Cambio Actual",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(15, 5))
        
        self.tipo_cambio_label = ctk.CTkLabel(
            exchange_frame,
            text=f"1 USD = ${self.tipo_cambio:.2f} MXN",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.tipo_cambio_label.pack(pady=5)
        
        self.actualizacion_label = ctk.CTkLabel(
            exchange_frame,
            text=f"Última actualización: {self.ultima_actualizacion}",
            font=ctk.CTkFont(size=12)
        )
        self.actualizacion_label.pack(pady=(0, 15))
        
        # Botón actualizar
        update_btn = ctk.CTkButton(
            exchange_frame,
            text="🔄 Actualizar Tipo de Cambio",
            command=self.obtener_tipo_cambio,
            height=35
        )
        update_btn.pack(pady=(0, 15))
        
        # Frame de conversión
        conversion_frame = ctk.CTkFrame(main_frame)
        conversion_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Selector de conversión
        ctk.CTkLabel(
            conversion_frame,
            text="Tipo de Conversión",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(20, 10))
        
        self.conversion_var = ctk.StringVar(value="MXN a USD")
        conversion_menu = ctk.CTkOptionMenu(
            conversion_frame,
            values=["MXN a USD", "USD a MXN"],
            variable=self.conversion_var,
            command=self.cambiar_conversion,
            width=200,
            height=35
        )
        conversion_menu.pack(pady=(0, 20))
        
        # Campo de entrada
        self.entrada_label = ctk.CTkLabel(
            conversion_frame,
            text="Cantidad en Pesos Mexicanos (MXN):",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.entrada_label.pack(pady=(0, 5))
        
        self.entrada = ctk.CTkEntry(
            conversion_frame,
            placeholder_text="Ingrese la cantidad",
            width=300,
            height=40,
            font=ctk.CTkFont(size=16)
        )
        self.entrada.pack(pady=(0, 15))
        self.entrada.bind("<KeyRelease>", self.convertir_en_tiempo_real)
        
        # Resultado
        self.resultado_label = ctk.CTkLabel(
            conversion_frame,
            text="Resultado:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.resultado_label.pack(pady=(0, 5))
        
        self.resultado = ctk.CTkLabel(
            conversion_frame,
            text="$0.00 USD",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#00ff00", "#00ff00")
        )
        self.resultado.pack(pady=(0, 0))
        
        # Frame de información adicional
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(fill="x", padx=20)
        
        info_text = """
💡 Información:
• Los tipos de cambio se actualizan en tiempo real
• Las conversiones son aproximadas
• Para transacciones reales, consulte con su banco
        """
        
        ctk.CTkLabel(
            info_frame,
            text=info_text,
            font=ctk.CTkFont(size=12),
            justify="left"
        ).pack(pady=0)
    
    def obtener_tipo_cambio(self):
        """Obtiene el tipo de cambio actual desde una API"""
        def fetch():
            try:
                # Usando una API gratuita para obtener el tipo de cambio
                response = requests.get(
                    "https://api.exchangerate-api.com/v4/latest/USD",
                    timeout=10
                )
                data = response.json()
                
                if 'rates' in data and 'MXN' in data['rates']:
                    self.tipo_cambio = data['rates']['MXN']
                    now = datetime.now()
                    self.ultima_actualizacion = now.strftime("%H:%M:%S")
                    
                    # Actualizar la interfaz en el hilo principal
                    self.root.after(0, self.actualizar_interfaz_tipo_cambio)
                else:
                    self.root.after(0, lambda: messagebox.showwarning(
                        "Advertencia", 
                        "No se pudo obtener el tipo de cambio. Usando valor por defecto."
                    ))
            except requests.exceptions.RequestException:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error de Conexión",
                    "No se pudo conectar al servicio de tipos de cambio.\nVerifique su conexión a internet."
                ))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error", 
                    f"Error inesperado: {str(e)}"
                ))
        
        # Ejecutar en un hilo separado para no bloquear la interfaz
        thread = threading.Thread(target=fetch, daemon=True)
        thread.start()
    
    def actualizar_interfaz_tipo_cambio(self):
        """Actualiza la interfaz con el nuevo tipo de cambio"""
        self.tipo_cambio_label.configure(text=f"1 USD = ${self.tipo_cambio:.2f} MXN")
        self.actualizacion_label.configure(text=f"Última actualización: {self.ultima_actualizacion}")
        
        # Reconvertir si hay algo en el campo de entrada
        if self.entrada.get():
            self.convertir()
    
    def cambiar_conversion(self, selection):
        """Cambia el tipo de conversión y actualiza las etiquetas"""
        if selection == "MXN a USD":
            self.entrada_label.configure(text="Cantidad en Pesos Mexicanos (MXN):")
            self.entrada.configure(placeholder_text="Ingrese la cantidad en MXN")
            self.resultado_label.configure(text="Resultado en Dólares (USD):")
        else:
            self.entrada_label.configure(text="Cantidad en Dólares Estadounidenses (USD):")
            self.entrada.configure(placeholder_text="Ingrese la cantidad en USD")
            self.resultado_label.configure(text="Resultado en Pesos (MXN):")
        
        # Limpiar campos y reconvertir si hay datos
        if self.entrada.get():
            self.convertir()
    
    def convertir_en_tiempo_real(self, event=None):
        """Convierte automáticamente mientras el usuario escribe"""
        self.convertir()
    
    def convertir(self):
        """Realiza la conversión de divisas"""
        try:
            cantidad_str = self.entrada.get().replace(",", "")
            
            if not cantidad_str:
                self.resultado.configure(text="$0.00")
                return
            
            cantidad = float(cantidad_str)
            
            if cantidad < 0:
                messagebox.showwarning("Advertencia", "La cantidad debe ser positiva")
                return
            
            if self.conversion_var.get() == "MXN a USD":
                # Convertir MXN a USD
                resultado = cantidad / self.tipo_cambio
                self.resultado.configure(text=f"${resultado:.2f} USD")
            else:
                # Convertir USD a MXN
                resultado = cantidad * self.tipo_cambio
                self.resultado.configure(text=f"${resultado:.2f} MXN")
                
        except ValueError:
            self.resultado.configure(text="Cantidad inválida")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión: {str(e)}")
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = CasaCambioApp()
    app.ejecutar()