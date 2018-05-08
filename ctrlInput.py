from pymouse import PyMouse
from pykeyboard import PyKeyboard


class ctrlInput:
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
        if x > 25 or y > 25 or x < -25 or y < -25:
            return
        self.m.move(self.pos_x() - x, self.pos_y() + y)

    def click_left(self):
        self.m.click(self.pos_x(), self.pos_y(), 1)

    def click_right(self):
        self.m.click(self.pos_x(), self.pos_y(), 2)

    def click_middle(self):
        self.m.click(self.pos_x(), self.pos_y(), 3)

    def type(self, string):
        self.k.type_string(string)

    def execute(self, cmd, *args):
        print("## executing: "+cmd)
        print('## cmd: '+cmd)
        # print('## args: '+str(*args))
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
