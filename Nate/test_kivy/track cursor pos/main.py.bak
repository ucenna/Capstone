from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
import CtrlSocket
import sys
s = CtrlSocket.ClientSocket(CtrlSocket.UDPSocket())
host = CtrlSocket.socket.gethostname()
port = 9999
s.connect((host, port))

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        tp = TrackPos()
        self.add_widget(tp)


class TrackPos(Widget):
    currentPos = ListProperty([0,0])

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
        return super(TrackPos, self).on_touch_move(touch)

class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TestApp().run()
