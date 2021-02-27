#from kivy.config import Config
#Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window

class HoverBehavior(object):

    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)


    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)


    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        #Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            #We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')


    def on_enter(self):
        pass

    def on_leave(self):
        pass


class HoverButton(Button,HoverBehavior):
    
    def on_enter(self, *arg):
        self.bg = self.background_normal
        self.background_normal=self.background_down

    def on_leave(self, *arg):
        self.background_normal=self.bg


class ScreenManager(ScreenManager):
    pass


class Intro(Screen):
    pass


class GameMenu(Screen):
    pass

class MiningMenu(Screen):
    pass

class MainApp(App):
    def build(self):
        Window.size = (1060,720)
        kv_file = Builder.load_file('app.kv')
        return kv_file


if __name__ == '__main__':
    LabelBase.register(name='Header', fn_regular="font/Uni Sans Heavy.ttf")
    LabelBase.register(name='Normal', fn_regular="font/WhitneyBold.ttf")

    MainApp().run()







