from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
import operator

class CalculatorWidget(BoxLayout):
    
    MathExpression = StringProperty("")
    StringOfMathExpression = MathExpression
    ListOfExpression = []


    def ButtonIsClicked(self, NumOrChar):
        self.StringOfMathExpression += NumOrChar

    def EvaluateMathExpression(self):
        
        for x in self.StringOfMathExpression:
            self.ListOfExpression.append(x)

        while len(self.ListOfExpression) > 2:
            #pEmdas
            i = 0
            while i < len(self.ListOfExpression):
                if self.ListOfExpression[i] == '^':
                    EvaluatedExpression = operator.pow(float(self.ListOfExpression[i-1]), float(self.ListOfExpression[i+1]))
                    self.ListOfExpression[i-1] = EvaluatedExpression
                    self.ListOfExpression.pop(i)
                    self.ListOfExpression.pop(i)
                else:
                    pass
                i+=1


            #peMDas 
            i = 0
            while i < len(self.ListOfExpression):

                if self.ListOfExpression[i] == '*':
                    EvaluatedExpression = operator.mul(float(self.ListOfExpression[i-1]), float(self.ListOfExpression[i+1]))
                    self.ListOfExpression[i-1] = EvaluatedExpression
                    self.ListOfExpression.pop(i)
                    self.ListOfExpression.pop(i)
                
                elif self.ListOfExpression[i] == '/':
                    EvaluatedExpression = operator.truediv(float(self.ListOfExpression[i-1]), float(self.ListOfExpression[i+1]))
                    self.ListOfExpression[i-1] = EvaluatedExpression
                    self.ListOfExpression.pop(i)
                    self.ListOfExpression.pop(i)
                else:
                    pass
                i+=1

            #pemdAS
            i = 0
            while i < len(self.ListOfExpression):

                if self.ListOfExpression[i] == '+':
                    EvaluatedExpression = operator.add(float(self.ListOfExpression[i-1]), float(self.ListOfExpression[i+1]))
                    self.ListOfExpression[i-1] = EvaluatedExpression
                    self.ListOfExpression.pop(i)
                    self.ListOfExpression.pop(i)
                
                elif self.ListOfExpression[i] == '-':
                    EvaluatedExpression = operator.sub(float(self.ListOfExpression[i-1]), float(self.ListOfExpression[i+1]))
                    self.ListOfExpression[i-1] = EvaluatedExpression
                    self.ListOfExpression.pop(i)
                    self.ListOfExpression.pop(i)
                else:
                    pass
                i+=1

        if int(self.ListOfExpression[0]) == float(self.ListOfExpression[0]):
            self.MathExpression = str(int(self.ListOfExpression[0]))
        else:
            self.MathExpression = str(self.ListOfExpression[0])

        print(self.MathExpression)
        print("hello")


class WidgetsExample(GridLayout):
    counter = 0
    counter_bool = BooleanProperty(False)
    my_text = StringProperty("0") 
    tb_my_text = StringProperty("OFF")
    #slider_value_txt = StringProperty("0")
    input_text = StringProperty("")

    def ButtonIsClicked(self):
        if self.counter_bool == False:
            self.counter += 0
        else:
            self.counter += 1
        
        self.my_text = str(self.counter)

    def ToggleButtonState(self, toggle_button):
        if toggle_button.state == "normal":
            self.tb_my_text = "OFF"
            self.counter_bool = False
        else:
            self.tb_my_text = "ON"
            self.counter_bool = True
        
    def SwitchActivated(self, switch_button):
        print("Switch: " + str(switch_button.active))
    
    #def OnSliderValue(self, slider):
    #    self.slider_value_txt = str(int(slider.value))
    #    print("Slider: " + str(int(slider.value)))

    def OnTextValidate(self, widget):
        self.input_text = widget.text

class GridLayoutExample(GridLayout):
    pass

class MainWidget(Widget):
    pass

class BoxLayoutExample(BoxLayout):
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
            Line(rectangle=(300, 200, 50, 50), width=2)
            self.rect = Rectangle(pos=(400, 400), size=(100,50))

    def OnButtonPress_MoveUntilBorder(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        difference = self.width - (x + w)
        move_distance = dp(20)

        if difference < move_distance:
            move_distance = difference

        x += move_distance
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.ball_speed_x = dp(1)
            self.ball_speed_y = dp(0.5)
            self.ball_size = dp(50)
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update_ball_position, 1/60)

    def on_size(self, *args):
        #print(str(self.width) + "|--|" + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update_ball_position(self, dt):
        x, y = self.ball.pos
        radius_x, radius_y = self.ball.size
        
        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.ball_speed_y = -self.ball_speed_y

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.ball_speed_x = -self.ball_speed_x
        
        if y < 0:
            y = 0
            self.ball_speed_y = -self.ball_speed_y
        
        if x < 0:
            x = 0
            self.ball_speed_x = -self.ball_speed_x
  
        self.ball.pos = (x+self.ball_speed_x, y+self.ball_speed_y)

    """Ball rebounds but when resized, it doesnt anymore        
        if x+radius_x == self.width:
            self.ball_speed_x = -self.ball_speed_x

        if x == 0:
            self.ball_speed_x = -self.ball_speed_x

        if y+radius_y == self.height:
            self.ball_speed_y = -self.ball_speed_y
        
        if y == 0:
            self.ball_speed_y = -self.ball_speed_y
        
        self.ball.pos = (x+self.ball_speed_x, y+self.ball_speed_y) 
    """

class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()