from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.config import Config
import requests
from datetime import datetime
import threading

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', True)

class CasaCambioApp(App):
    def __init__(self):
        super().__init__()
        self.tipo_cambio = 17.5
        self.ultima_actualizacion = "Manual"
        self.conversion_type = "MXN a USD"
        
    def build(self):
        self.title = "Casa de Cambio MXN ↔ USD"
        
        from kivy.uix.scrollview import ScrollView
        scroll = ScrollView()
        
        main_layout = BoxLayout(
            orientation='vertical',
            padding=[dp(20), dp(20)],
            spacing=dp(10),
            size_hint_y=None
        )
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        title = Label(
            text='Casa de Cambio',
            font_size=dp(28),
            size_hint_y=None,
            height=dp(60),
            bold=True,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(title)
        
        subtitle = Label(
            text='Pesos Mexicanos u Dólares USD',
            font_size=dp(14),
            size_hint_y=None,
            height=dp(40),
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(subtitle)
        
        tipo_cambio_title = Label(
            text='Tipo de Cambio Actual',
            font_size=dp(18),
            size_hint_y=None,
            height=dp(40),
            bold=True,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(tipo_cambio_title)
        
        self.tipo_cambio_label = Label(
            text=f'1 USD = ${self.tipo_cambio:.2f} MXN',
            font_size=dp(22),
            size_hint_y=None,
            height=dp(50),
            bold=True,
            color=(0, 1, 0.5, 1)
        )
        main_layout.add_widget(self.tipo_cambio_label)
        
        self.actualizacion_label = Label(
            text=f'Última actualización: {self.ultima_actualizacion}',
            font_size=dp(12),
            size_hint_y=None,
            height=dp(30),
            color=(0.6, 0.6, 0.6, 1)
        )
        main_layout.add_widget(self.actualizacion_label)
        
        update_btn = Button(
            text='Actualizar Tipo de Cambio',
            size_hint_y=None,
            height=dp(50),
            font_size=dp(14),
            background_color=(0.2, 0.6, 1, 1)
        )
        update_btn.bind(on_press=self.obtener_tipo_cambio)
        main_layout.add_widget(update_btn)
        
        conversion_title = Label(
            text='Conversión de Divisas',
            font_size=dp(18),
            size_hint_y=None,
            height=dp(40),
            bold=True,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(conversion_title)
        
        conversion_label = Label(
            text='Tipo de Conversión:',
            font_size=dp(14),
            size_hint_y=None,
            height=dp(35),
            bold=True,
            color=(0.9, 0.9, 0.9, 1)
        )
        main_layout.add_widget(conversion_label)
        
        self.conversion_spinner = Spinner(
            text='MXN a USD',
            values=['MXN a USD', 'USD a MXN'],
            size_hint_y=None,
            height=dp(45),
            font_size=dp(16),
            background_color=(0.3, 0.3, 0.3, 1)
        )
        self.conversion_spinner.bind(text=self.cambiar_conversion)
        main_layout.add_widget(self.conversion_spinner)
        
        self.entrada_label = Label(
            text='Cantidad en Pesos Mexicanos (MXN):',
            font_size=dp(14),
            size_hint_y=None,
            height=dp(35),
            bold=True,
            color=(0.9, 0.9, 0.9, 1)
        )
        main_layout.add_widget(self.entrada_label)
        
        self.entrada = TextInput(
            hint_text='Ingrese la cantidad...',
            size_hint_y=None,
            height=dp(45),
            font_size=dp(16),
            multiline=False,
            input_filter='float',
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1)
        )
        self.entrada.bind(text=self.convertir_en_tiempo_real)
        main_layout.add_widget(self.entrada)
        
        resultado_title = Label(
            text='Resultado:',
            font_size=dp(16),
            size_hint_y=None,
            height=dp(35),
            bold=True,
            color=(0.9, 0.9, 0.9, 1)
        )
        main_layout.add_widget(resultado_title)
        
        self.resultado = Label(
            text='$0.00 USD',
            font_size=dp(26),
            size_hint_y=None,
            height=dp(60),
            bold=True,
            color=(0, 1, 0.5, 1)
        )
        main_layout.add_widget(self.resultado)
        
        info = Label(
            text='Información:\n'
                 '• Los tipos de cambio se actualizan en tiempo real\n'
                 '• Las conversiones son aproximadas\n'
                 '• Para transacciones reales, consulte su banco',
            font_size=dp(12),
            size_hint_y=None,
            height=dp(100),
            text_size=(dp(350), None),
            halign='left',
            valign='middle',
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(info)
        
        spacer = Label(
            text='',
            size_hint_y=None,
            height=dp(20)
        )
        main_layout.add_widget(spacer)
        
        copy = Label(
            text='By @Angel Cuevas\n',
            font_size=dp(12),
            size_hint_y=None,
            height=dp(100),
            text_size=(dp(350), None),
            halign='center',
            valign='center',
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(copy)

        scroll.add_widget(main_layout)
        
        Clock.schedule_once(lambda dt: self.obtener_tipo_cambio(), 2)
        
        return scroll
    
    def obtener_tipo_cambio(self, instance=None):
        """Obtiene el tipo de cambio actual desde una API"""
        def fetch():
            try:
                print("Obteniendo tipo de cambio...")
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
                    Clock.schedule_once(lambda dt: self.actualizar_interfaz_tipo_cambio(), 0)
                    print(f"Tipo de cambio actualizado: {self.tipo_cambio}")
                else:
                    Clock.schedule_once(lambda dt: self.mostrar_popup(
                        "Advertencia", 
                        "No se pudo obtener el tipo de cambio.\nUsando valor por defecto."
                    ), 0)
            except requests.exceptions.RequestException as e:
                Clock.schedule_once(lambda dt: self.mostrar_popup(
                    "Error de Conexión",
                    f"No se pudo conectar al servicio de tipos de cambio.\n\nError: {str(e)}\n\nVerifique su conexión a internet."
                ), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.mostrar_popup(
                    "Error",
                    f"Error inesperado: {str(e)}"
                ), 0)
        
        # Ejecutar en un hilo separado
        thread = threading.Thread(target=fetch, daemon=True)
        thread.start()
    
    def actualizar_interfaz_tipo_cambio(self):
        """Actualiza la interfaz con el nuevo tipo de cambio"""
        self.tipo_cambio_label.text = f"1 USD = ${self.tipo_cambio:.2f} MXN"
        self.actualizacion_label.text = f"Última actualización: {self.ultima_actualizacion}"
        
        # Reconvertir si hay algo en el campo de entrada
        if self.entrada.text:
            self.convertir()
    
    def cambiar_conversion(self, spinner, text):
        """Cambia el tipo de conversión"""
        self.conversion_type = text
        if text == "MXN a USD":
            self.entrada_label.text = "Cantidad en Pesos Mexicanos (MXN):"
            self.entrada.hint_text = "Ingrese la cantidad en MXN..."
        else:
            self.entrada_label.text = "Cantidad en Dólares Estadounidenses (USD):"
            self.entrada.hint_text = "Ingrese la cantidad en USD..."
        
        if self.entrada.text:
            self.convertir()
    
    def convertir_en_tiempo_real(self, instance, value):
        """Convierte automáticamente mientras el usuario escribe"""
        if value:
            # Cancelar conversiones previas programadas
            Clock.unschedule(self.convertir)
            # Programar nueva conversión con un pequeño delay
            Clock.schedule_once(lambda dt: self.convertir(), 0.5)
    
    def convertir(self, instance=None):
        """Realiza la conversión de divisas"""
        try:
            cantidad_str = self.entrada.text.replace(",", "").strip()
            
            if not cantidad_str:
                if self.conversion_type == "MXN a USD":
                    self.resultado.text = "$0.00 USD"
                else:
                    self.resultado.text = "$0.00 MXN"
                return
            
            cantidad = float(cantidad_str)
            
            if cantidad < 0:
                self.mostrar_popup("Advertencia", "La cantidad debe ser positiva")
                return
            
            if self.conversion_type == "MXN a USD":
                resultado = cantidad / self.tipo_cambio
                self.resultado.text = f"${resultado:,.2f} USD"
            else:
                resultado = cantidad * self.tipo_cambio
                self.resultado.text = f"${resultado:,.2f} MXN"
                
        except ValueError:
            self.resultado.text = "❌ Cantidad inválida"
        except Exception as e:
            self.mostrar_popup("Error", f"Error en la conversión: {str(e)}")
    
    def mostrar_popup(self, titulo, mensaje):
        """Muestra un popup con un mensaje"""
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        msg_label = Label(
            text=mensaje, 
            text_size=(dp(300), None),
            halign='center',
            valign='middle',
            font_size=dp(14)
        )
        content.add_widget(msg_label)
        
        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.85, 0.6),
            auto_dismiss=False
        )
        
        btn_ok = Button(
            text='OK',
            size_hint=(None, None),
            size=(dp(100), dp(45)),
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_ok.bind(on_press=popup.dismiss)
        content.add_widget(btn_ok)
        
        popup.open()

if __name__ == '__main__':
    try:
        CasaCambioApp().run()
    except Exception as e:
        print(f"Error al ejecutar la aplicación: {e}")
        input("Presiona Enter para salir...")
