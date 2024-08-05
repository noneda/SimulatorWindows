from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label

class BlueDeathScreen(Widget):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.canvas.clear()
        with self.canvas:
            self.bg_color = Color(0, 0, 1, 1)  # Fondo azul inicial
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        # Configura el texto
        self.label = Label(text='DEAD',
                           font_size=100,
                           color=(1, 1, 1, 1),
                           size_hint=(None, None))
        self.label.size = self.label.texture_size
        self.add_widget(self.label)
        
        # Centrar el texto inicialmente
        self.center_label()

        # Programar la animación
        Clock.schedule_interval(self.update_animation, 1 / 60)
        self.anim_duration = 4
        self.start_time = Clock.get_time()

    def update_animation(self, dt):
        elapsed = Clock.get_time() - self.start_time
        if elapsed < self.anim_duration:
            anim_time = (elapsed % 1) / 0.5
            if anim_time < 0.5:
                self.bg_color.rgba = (0, 0, 1, 1)  # Azul
            else:
                self.bg_color.rgba = (1, 1, 1, 1)  # Blanco

            text_anim_time = (elapsed % 1) / 0.5
            if text_anim_time < 0.5:
                self.label.color = (1, 1, 1, 1)  # Blanco
            else:
                self.label.color = (0, 0, 0, 1)  # Negro
        else:
            Clock.unschedule(self.update_animation)
            app = self.app.get_running_app()
            app.stop()  # Termina la aplicación

    def on_size(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.center_label()

    def on_pos(self, *args):
        self.rect.pos = self.pos

    def center_label(self):
        # Centra el texto en el Widget
        self.label.center_x = self.width / 2
        self.label.center_y = self.height / 2
