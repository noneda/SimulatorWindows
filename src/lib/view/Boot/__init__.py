import time
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class AnimationWidget(Widget):
    def __init__(self,App, **kwargs):
        super().__init__(**kwargs)
        self.rect = None
        self.App = App
        self.start_time = time.time()
        with self.canvas:
            Color(0, 0, 0)
            self.rect = Rectangle(pos=(0, 0), size=(800, 400))
        Clock.schedule_interval(self.update_animation, 1 / 60)

    def start(self):
        self.start_time = time.time()

    def update_animation(self, dt):
        elapsed = time.time() - self.start_time
        if elapsed < 3:
            with self.canvas:
                Color(0, 0, 0)
                self.rect = Rectangle(pos=(0, 0), size=(800, 400))
        elif elapsed < 7:
            size = 100
            pos = (self.width / 2 - size / 2, self.height / 2 - size / 2)
            with self.canvas:
                Color(1, 1, 1)
                self.rect = Rectangle(pos=pos, size=(size, size))
        else:
            Clock.unschedule(self.update_animation)
            app = self.App.get_running_app()
            app.switch_to_desktop()