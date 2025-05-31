from kivy.app import App
from kivy.lang import Builder

UI = Builder.load_file("screen.kv")

class Interface(App):
    def build(self):
        return UI
    
Interface().run()