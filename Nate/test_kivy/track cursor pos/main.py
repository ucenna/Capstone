from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
import CtrlSocket
import sys
s = CtrlSocket.ClientSocket(CtrlSocket.UDPSocket())
host = CtrlSocket.socket.gethostname()
port = 9999
s.connect((host, port))

currentPos = ListProperty([0,0])

class RootWidget(FloatLayout):
    currentPos = [0, 0]

    def leftClick(self, touch):
        sendMsg = 'OPENCAST '+'click_left()'
        sendMsg = sendMsg.encode('ascii')
        s.broadcast(sendMsg, port)

    def rightClick(self, touch):
        sendMsg = 'OPENCAST '+'click_right()'
        sendMsg = sendMsg.encode('ascii')
        s.broadcast(sendMsg, port)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            prevpos = self.currentPos
            self.currentPos = touch.pos
            relativePos = [prevpos[0]-self.currentPos[0], prevpos[1]-self.currentPos[1]]
            print('sending currentPos to PC: '+str(relativePos))
            sendMsg = 'OPENCAST '+'rel_move('+str(int(relativePos[0]))+','+str(int(relativePos[1]))+')'
            sendMsg = sendMsg.encode('ascii')
            s.broadcast(sendMsg, 9999)
            return True


    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        grid = GridLayout(cols=2, row_force_default=True, row_default_height=50)

        leftClick = Button(
        text='Left Click',
        size_hint=(.5,.25))
        leftClick.bind(on_press=self.leftClick)
        grid.add_widget(leftClick)

        rightClick = Button(
        text='Right Click',
        size_hint=(.5,.25),
        pos_hint={'right': .5})
        rightClick.bind(on_press=self.rightClick)
        grid.add_widget(rightClick)

        trackPad = Widget()
        trackPad.bind(on_touch_move=self.on_touch_move)
        self.add_widget(trackPad)

        self.add_widget(grid)


class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TestApp().run()
