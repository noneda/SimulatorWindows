from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window



class Process(Widget):
    def __init__(self, **kwargs):
        super(Process, self).__init__(**kwargs)
        self.size = (200, 100)  # Tamaño del proceso
        self.pos = (Window.width / 2 - self.size[0] / 2, Window.height / 2 - self.size[1] / 2)  # Centrar al inicio
        with self.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # Fondo gris
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.label = Label(text='Proceso', center=self.center)
        self.add_widget(self.label)

        self.dragging = False
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(on_touch_down=self.on_touch_down, on_touch_move=self.on_touch_move, on_touch_up=self.on_touch_up)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.label.center = self.center

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dragging = True
            return True
        return super(Process, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.dragging:
            self.center_x = touch.x
            self.center_y = touch.y
            return True
        return super(Process, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.dragging:
            self.dragging = False
            return True
        return super(Process, self).on_touch_up(touch)
