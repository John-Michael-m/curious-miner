from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class ScreenManager(ScreenManager):
    pass

class Intro(Screen):
    pass

class GameMenu(Screen):
    pass

class MainApp(App):
    def build(self):
        kv_file = Builder.load_file('app.kv')
        return kv_file

if __name__ == '__main__':
    MainApp().run()







