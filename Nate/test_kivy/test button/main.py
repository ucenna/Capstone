import kivy
kivy.require('1.10.0')
from kivy.app import App        # import kivy and kivy.app (kivy.app is needed so kivy runs successfully, just trust it)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os

class RunCMD(BoxLayout):    # create root widget with BoxLayout
    def __init__(self):                 #
        super(RunCMD, self).__init__()  # define and call constructor for boxlayout class

    def openFirefox(self):      # run 'firefox.exe' from original file directory
        print("Running 'openFirefox()' now")
        os.system("cd\Program Files\Mozilla Firefox && firefox.exe")
        print("Firefox opened")
        print(kivy.__version__)

class ActionApp(App):       # set up event loop for app
    def build(self):        #
        return RunCMD()     # override build function and return instance of 'RunCMD' class as root widget

test = ActionApp()      #
                        #
test.run()              # run the app
