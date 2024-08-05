from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from .Boot import AnimationWidget
from .Desktop import DesktopWidget
from .ScreenDead import BlueDeathScreen

class ComputerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.animation_widget = AnimationWidget(self)
        self.layout.add_widget(self.animation_widget)
        Clock.schedule_once(self.start_animation, 0)  # Start animation after the first frame
        return self.layout

    def start_animation(self, dt):
        self.animation_widget.start()

    def switch_to_desktop(self):
        self.root.clear_widgets()
        self.root.add_widget(DesktopWidget(self))

    def siwth_to_dead(self):
        self.root.clear_widgets()
        self.root.add_widget(BlueDeathScreen(self))

    def Off(self):
        App.get_running_app().stop()
