from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock
from .process import Process

class DesktopWidget(Widget):

    def __init__(self, App, **kwargs):
        super(DesktopWidget, self).__init__(**kwargs)
        
        self.App = App

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
        self.taskbar_pos_x = 40 + 10 
        with self.start_button.canvas:
            self.button_color = Color(0, 1, 0, 1)  # Color verde
            self.button = Ellipse(pos=self.start_button.pos, size=self.start_button.size)
        self.start_button.bind(pos=self.update_button, size=self.update_button)
        self.start_button.bind(on_touch_down=self.on_start_button_press)
        self.taskbar.add_widget(self.start_button)

        # Etiqueta para mostrar la cuenta regresiva
        self.counter_label = Label(text='5', font_size='40sp', size_hint=(None, None), size=(200, 100))
        self.add_widget(self.counter_label)
        self.counter_label.canvas.before.add(Color(0.5, 0.5, 0.5, 1))  # Fondo gris
        self.counter_label_rect = Rectangle(size=self.counter_label.size)
        self.counter_label.canvas.before.add(self.counter_label_rect)
        self.counter_label.opacity = 0  # Hacer que el cuadro de contador sea invisible al inicio

        # Inicializar el contador
        self.counter_event = None
        self.counter = 5

        self.launch_button = Button(text='Abrir Proceso', size_hint=(None, None), size=(120, 40), pos=(50, Window.height - 100))
        self.launch_button.bind(on_press=self.create_process)
        self.add_widget(self.launch_button)

        # Actualizar la posición del contador
        self.update_label_position()

        self.process  = []
        self.taskbar_icons  = []

    def update_label_position(self, *args):
        # Centrar el label
        self.counter_label.center_x = Window.width / 2
        self.counter_label.center_y = Window.height / 2
        self.counter_label_rect.pos = self.counter_label.pos

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

        if self.counter == 0:
            app = self.App.get_running_app()
            app.Off()

    def create_process(self, instance):
        if len(self.process) <= 5:
            obj = Process()
            self.process.append(obj)
            self.add_widget(obj)
            self.add_process_to_taskbar(obj)
        else:
            app = self.App.get_running_app()
            app.siwth_to_dead()


    def add_process_to_taskbar(self, process):
        taskbar_icon = Widget(size=(40, 40), pos=( self.taskbar_pos_x, 0))
        self.taskbar_pos_x += 50
        with taskbar_icon.canvas:
            Color(*process.color)  # Color gris
            Rectangle(size=taskbar_icon.size, pos=taskbar_icon.pos)
        taskbar_icon.process = process
        taskbar_icon.color = process.color
        taskbar_icon.bind(on_touch_down=self.on_taskbar_icon_touch_down)

        self.taskbar.add_widget(taskbar_icon)
        self.taskbar_icons.append(taskbar_icon)

    def on_taskbar_icon_touch_down(self, instance, touch):
        if instance.collide_point(*touch.pos):
            process = instance.process
            if process in self.process:
                self.remove_process(process)
                self.taskbar.remove_widget(instance)
                self.taskbar_icons.remove(instance)

    def remove_process(self, process):
        if process in self.process:
            self.process.remove(process)
            self.remove_widget(process)
            self.reorder_taskbar_icons()

    def reorder_taskbar_icons(self):
        self.taskbar_pos_x = 50
        for icon in self.taskbar_icons:
            icon.pos = (self.taskbar_pos_x, 0)
            icon.canvas.clear()
            with icon.canvas:
                Color(*icon.color)  # Color gris
                Rectangle(size=icon.size, pos=icon.pos)
            self.taskbar_pos_x += 50
