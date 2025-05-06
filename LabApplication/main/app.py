import random

from kivy.app import App
from kivy.metrics import sp
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class LabCounterGridLayout(GridLayout):
    counter_int: NumericProperty = NumericProperty(1)
    random_float: NumericProperty = NumericProperty(1.0)
    state_str: StringProperty = StringProperty("OFF")
    enable_button: BooleanProperty = BooleanProperty(True)
    enable_slider: BooleanProperty = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def increment_counter(self) -> None:
        if self.enable_button is False:
            self.counter_int += 1

    def get_random_float_value(self) -> None:
        self.random_float = random.random()

    def execute_toggle_button_behaviour(self, toggle_button: ToggleButton) -> None:
        if toggle_button.state == "down":
            self.state_str = "ON"
            self.enable_button = False
        else:
            self.state_str = "OFF"
            self.enable_button = True

    def on_switch_active(self, switch_widget: Switch) -> None:
        if switch_widget.active:
            self.enable_slider = False
        else:
            self.enable_slider = True


class LabStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        num_buttons: int = 100
        self.orientation: str = "tb-lr"
        self.spacing: tuple[int, int] = (20, 20)
        self.padding: list[float] = [sp(20), sp(20), sp(20), sp(20)]
        for button_num in range(0, num_buttons):
            button: Button = Button(
                text=f"B{button_num + 1}",
                size_hint=(None, None),
                size=(sp(100), sp(100))
            )
            self.add_widget(widget=button)


class LabAnchorLayout(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LabBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LabWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LabApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def main() -> int:
    try:

        lab_app: LabApp = LabApp()
        lab_app.run()

    except Exception as e:
        print(f"Exception Thrown: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
