from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

import random
colors = [
    (255, 255, 255),  # Blanco
    (255, 0, 0),      # Rojo
    (0, 255, 0),      # Verde
    (255, 255, 0),    # Amarillo
    (0,0,0)
]

class Process(Widget):
    def __init__(self, **kwargs):
        super(Process, self).__init__(**kwargs)
        self.size = (200, 100)  # Tamaño del proceso
        self.pos = (Window.width / 2 - self.size[0] / 2, Window.height / 2 - self.size[1] / 2)  # Centrar al inicio
        self.dragging = False
        self.color = random.choice(colors)

        with self.canvas.before:
            Color(*self.color)  # Fondo gris
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dragging = True
            return True
        return super(Process, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.dragging:
            self.pos = (touch.x - self.width / 2, touch.y - self.height / 2)
            return True
        return super(Process, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.dragging:
            self.dragging = False
            return True
        return super(Process, self).on_touch_up(touch)