from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock

class DesktopWidget(Widget):
    def __init__(self, **kwargs):
        super(DesktopWidget, self).__init__(**kwargs)    
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock

class DesktopWidget(Widget):
    def __init__(self, **kwargs):
        super(DesktopWidget, self).__init__(**kwargs)
        
        # Fondo azul
        with self.canvas.before:
            Color(0, 0, 1, 1)  # Color azul
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        # Barra de tareas
        self.taskbar = Widget(size=(800, 40), pos=(0, 0))
        with self.taskbar.canvas:
            Color(0.5, 0.5, 0.5, 1)  # Color gris
            Rectangle(size=self.taskbar.size, pos=self.taskbar.pos)
        self.add_widget(self.taskbar)

        # Botón de inicio
        self.start_button = Widget(size=(40, 40), pos=(0, 0))
        with self.start_button.canvas:
            self.button_color = Color(0, 1, 0, 1)  # Color verde
            self.button = Ellipse(pos=self.start_button.pos, size=self.start_button.size)
        self.start_button.bind(pos=self.update_button, size=self.update_button)
        self.start_button.bind(on_touch_down=self.on_start_button_press)
        self.taskbar.add_widget(self.start_button)

        # Etiqueta para mostrar la cuenta regresiva
        self.counter_label = Label(text='5', font_size='40sp', size_hint=(None, None), size=(200, 100), pos=(self.start_button.width + 50, 50))
        self.counter_label.canvas.before.add(Color(0.5, 0.5, 0.5, 1))  # Fondo gris
        self.counter_label_rect = Rectangle(size=self.counter_label.size, pos=self.counter_label.pos)
        self.counter_label.canvas.before.add(self.counter_label_rect)
        self.counter_label.opacity = 0  # Hacer que el cuadro de contador sea invisible al inicio
        self.add_widget(self.counter_label)

        # Inicializar el contador
        self.counter_event = None
        self.counter = 5

    def update_button(self, instance, value):
        self.button.pos = instance.pos
        self.button.size = instance.size

    def on_start_button_press(self, instance, touch):
        if self.start_button.collide_point(*touch.pos):
            if self.counter_event is None:
                # Iniciar la cuenta regresiva
                self.counter = 5
                self.counter_event = Clock.schedule_interval(self.update_counter, 1)
                # Cambiar color del botón a rojo
                self.button_color.r = 1
                self.button_color.g = 0
                self.button_color.b = 0
                # Mostrar el cuadro de contador
                self.counter_label.opacity = 1
            else:
                # Cancelar la cuenta regresiva
                if self.counter_event is not None:
                    self.counter_event.cancel()
                    self.counter_event = None
                    self.counter_label.text = '5'
                    # Cambiar color del botón a verde
                    self.button_color.r = 0
                    self.button_color.g = 1
                    self.button_color.b = 0
                    # Ocultar el cuadro de contador
                    self.counter_label.opacity = 0

    def update_counter(self, dt):
        self.counter -= 1
        self.counter_label.text = str(self.counter)
        if self.counter <= 0:
            # Detener el contador y limpiar el evento
            if self.counter_event is not None:
                self.counter_event.cancel()
                self.counter_event = None
            # Cambiar color del botón a verde
            self.button_color.r = 0
            self.button_color.g = 1
            self.button_color.b = 0
            self.counter_label.text = '0'
            # Ocultar el cuadro de contador
            self.counter_label.opacity = 0