from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.stencilview import StencilView


class DrawInputWidget(StencilView):

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("RELEASED!",touch)


class VitalSignDrawer(App):

    def build(self):
        self.x_data_array = []
        self.y_data_array = []

        self.output_file_name = 'test.txt'

        parent = BoxLayout(orientation = 'vertical')
        draw_area = DrawInputWidget()
        draw_area.size_hint = (1, 0.8)

        option_layout = BoxLayout(orientation = 'horizontal', size_hint = (1, 0.2))
        inputText = TextInput(multiline = False)
        inputText.bind(text = self.text_changed_handler)
        inputText.text = 'Enter the name of output file here'

        clearBtn = Button(text = 'Clear')
        clearBtn.bind(on_release = lambda obj : draw_area.canvas.clear())

        applyBtn = Button(text = 'Apply')
        applyBtn.bind(on_release = self.apply_data)

        option_layout.add_widget(clearBtn)
        option_layout.add_widget(inputText)
        option_layout.add_widget(applyBtn)

        parent.add_widget(draw_area)
        parent.add_widget(option_layout)

        return parent

    def apply_data(self, obj):
        print('Applied')
        print(self.output_file_name)

    def text_changed_handler(self, instance, text):
        self.output_file_name = text
        return text

if __name__ == '__main__':
    VitalSignDrawer().run()