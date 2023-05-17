from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget 
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button 
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Clock

class WidgetsExample(GridLayout):
    count = 0
    count_state = BooleanProperty(False)
    my_text = StringProperty(str(count))
    text_input_str = StringProperty("fool")
    # slider_value_txt = StringProperty("50")

    def on_button_click(self):
        if self.count_state:
            self.count += 1
            self.my_text = str(self.count)

    def on_togle_button(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_state = False
            
        else:
            widget.text = "ON"
            self.count_state = True
    
    def on_switch_active(self,widget):
        print("switch: " + str(widget.active))
    
    # def on_slider_value(self, widget):
        # self.slider_value_txt = str(int(widget.value))
    
    def on_text_validate(self,widget):
        self.text_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation="lr-bt"

        for i in range(100):
            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    """  def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(50, 50, 200, 250), width=2)
            Color(0,1,0)
            Line(circle=(200,100,40), width=2)
            Line(rectangle=(350,250,75,50), width=5)
            self.rect = Rectangle(pos=(350,100), size=(75,50))
    
    def on_button_a_click(self):
        # print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size

        inc = dp(10)
        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
        
        x += inc
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=(self.center), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    
    def on_size(self, *args):
        print("on size: " + str(self.width) + "," + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)
    
    def update(self, dt):
        # print("update")
        x, y = self.ball.pos
        w, h = self.ball.size

        x += self.vx
        y += self.vy
        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx
        
        self.ball.pos = (x, y)

TheLabApp().run()