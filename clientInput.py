from pymouse import PyMouse
from pykeyboard import PyKeyboard


class clientInput:
    m = PyMouse()
    k = PyKeyboard()

    def pos_x(self):
        x, y = self.m.position()
        return x

    def pos_y(self):
        x, y = self.m.position()
        return y

    def rel_move(self, x=None, y=None):
        if x is None:
            x = 0
        if y is None:
            y = 0
        self.m.move(self.pos_x() + x, self.pos_y() + y)

    def execute(self, cmd, *args):
        print("## executing: "+cmd)
        print('## cmd: '+cmd)
        print('## args: '+str(*args))
        try:
            if args:
                result = getattr(self, cmd)(*args)
            else:
                result = getattr(self, cmd)()
            successMsg = str(result)
            if result is None:
                successMsg = 'Success'
            print('## result: '+successMsg)
            return result
        except AttributeError:
            print('## Result: Error: No such cmd')