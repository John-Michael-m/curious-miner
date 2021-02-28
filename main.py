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
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

import random

GOLD = 0

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
    def show_popup(self):
        content = IntroPopup()
        self.popup = Popup(title='How To Play', content=content, 
                   size_hint=(None,None),size=(600,200), 
                   title_font='font/WhitneyBold.ttf')
        self.popup.open()


class IntroPopup(FloatLayout):
    pass


class GameMenu(Screen):
    global GOLD
    gold = ObjectProperty(None)

    house = ObjectProperty(None)
    car = ObjectProperty(None)
    emerald = ObjectProperty(None)
    watch = ObjectProperty(None)
    goblet = ObjectProperty(None)
    pokeball = ObjectProperty(None)
    potion = ObjectProperty(None)
    sandwich = ObjectProperty(None)

    def on_enter(self):
        self.update_gold()

    def update_gold(self):
        self.gold.text = str(GOLD)
    
    def buy(self, item, amount):
        global GOLD
        if GOLD >= amount:
            GOLD -= amount
            self.update_gold()
            self.update_item(item)

    def update_item(self, item):
        item.color = (1,1,1,1)
        


class MiningMenu(Screen):
    gold = ObjectProperty(None)
    counter = ObjectProperty(None)


    def on_enter(self):
        self.update_gold()

        #timer
        self.counter.text = '60'
        self.event = Clock.schedule_interval(self.update_label, 1)


    def update_gold(self):
        self.gold.text = str(GOLD)
    
    def update_label(self, *args):
        global GOLD
        #Update the timer label  
        time = int(self.counter.text) - 1
        self.counter.text = str(time)

        if time == 0:
            GOLD * 1.2
            Clock.unschedule(self.event)
            self.manager.current = 'GameMenu'
    



class MainApp(App):

    def on_start(self):
        self.sound = SoundLoader.load('music.mp3')
        self.sound.volume = 0.1
        self.sound.loop = True
        self.sound.play()

    def build(self):
        Window.size = (1060,720)
        kv_file = Builder.load_file('app.kv')
        return kv_file


if __name__ == '__main__':
    LabelBase.register(name='Header', fn_regular="font/VIDEOPHREAK.ttf")
    LabelBase.register(name='Normal', fn_regular="font/WhitneyBold.ttf")

    MainApp().run()

    
    
   









