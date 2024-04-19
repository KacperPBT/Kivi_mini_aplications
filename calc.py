from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def get_last(self):
        prior = self.ids.calc_input.text
        if "+" in prior:
            num_list = prior.split("+")
            prior = num_list[-1]
        
        if "/" in prior:
            num_list = prior.split("/")
            prior = num_list[-1]
        if "*" in prior:
            num_list = prior.split("*")
            prior = num_list[-1]
        if "-" in prior:
            num_list = prior.split("-")
            prior = num_list[-1]
        return prior

    def percent(self):
        self.ids.calc_input.text += "*0.01*"

    def clear(self):
       self.ids.calc_input.text = '0'

    def remove(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]
        if prior[:-1] == '' or prior == "Error":
            self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if prior == '0' or prior == "Error":
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    
    def pos_neg(self):
        prior = self.ids.calc_input.text
        prior_l = self.get_last()
        if prior == prior_l:
            self.ids.calc_input.text = f"-{prior}"
        elif f"-{prior_l}" == prior:
            self.ids.calc_input.text = prior_l
        

    def dot(self):
        if self.ids.calc_input.text == "Error":
            self.ids.calc_input.text = '0'
        prior = self.get_last()
        if "." in prior:
            pass
        else:
            self.ids.calc_input.text += '.'

    def math_operator(self, operator):
        if self.ids.calc_input.text == "Error":
            self.ids.calc_input.text = '0'
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{operator}'

    def equal(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            answer = round(answer, 3)
            self.ids.calc_input.text = f'{answer}'
        except:
            self.ids.calc_input.text = 'Error'
                

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()