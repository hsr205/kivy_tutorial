from kivy.app import App
from kivy.metrics import sp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


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
