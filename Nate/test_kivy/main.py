

#this import is necessary for all Apps(just trust this)
from kivy.app import App
#will save "drop point" of widget being moved
from kivy.uix.scatter import Scatter
#imports label
from kivy.uix.label import Label
#allows user to move widget anywhere on screen
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello World",
                    font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == "__main__":
    TestApp().run()
